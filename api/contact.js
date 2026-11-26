// Vercel serverless function: emails contact form submissions through Resend.
// Required env vars: RESEND_API_KEY, CONTACT_TO, CONTACT_FROM.

const escape = (s) =>
  String(s).replace(/[&<>"']/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' })[c]);

module.exports = async (req, res) => {
  if (req.method !== 'POST') {
    res.setHeader('Allow', 'POST');
    return res.status(405).json({ error: 'Method not allowed.' });
  }

  const body = req.body && typeof req.body === 'object' ? req.body : {};
  const [name, email, agency, problem, website] = ['name', 'email', 'agency', 'problem', 'website'].map((k) =>
    body[k] == null ? '' : String(body[k])
  );

  // Honeypot: bots fill the hidden field. Pretend it worked.
  if (website) return res.status(200).json({ ok: true });

  if (!name.trim() || !email.trim() || !problem.trim()) {
    return res.status(400).json({ error: 'Please fill in your name, email and the service.' });
  }
  if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email) || name.length > 200 || agency.length > 200 || problem.length > 5000) {
    return res.status(400).json({ error: 'Please check your details.' });
  }

  const { RESEND_API_KEY, CONTACT_TO, CONTACT_FROM } = process.env;
  if (!RESEND_API_KEY || !CONTACT_TO || !CONTACT_FROM) {
    console.error('Contact form is missing RESEND_API_KEY, CONTACT_TO or CONTACT_FROM.');
    return res.status(500).json({ error: 'The form is not set up yet.' });
  }

  const response = await fetch('https://api.resend.com/emails', {
    method: 'POST',
    headers: { Authorization: `Bearer ${RESEND_API_KEY}`, 'Content-Type': 'application/json' },
    body: JSON.stringify({
      from: CONTACT_FROM,
      to: CONTACT_TO.split(',').map((s) => s.trim()),
      reply_to: email,
      subject: `New service enquiry from ${name}${agency ? ` (${agency})` : ''}`,
      text: `Name: ${name}\nEmail: ${email}\nAgency: ${agency || '-'}\n\n${problem}`,
      html: `<p><b>Name:</b> ${escape(name)}<br><b>Email:</b> ${escape(email)}<br><b>Agency:</b> ${escape(agency || '-')}</p><p style="white-space: pre-wrap">${escape(problem)}</p>`,
    }),
  });

  if (!response.ok) {
    console.error('Resend error', response.status, await response.text());
    return res.status(502).json({ error: 'We couldn’t send your message.' });
  }

  return res.status(200).json({ ok: true });
};
