const nodemailer = require('nodemailer');

export default async function handler(req, res) {
  if (req.method !== 'POST') {
    return res.status(405).send('Method Not Allowed');
  }
  const { name, mobile, age, institute, course, address, roomType, additionalInfo } = req.body;

  // Use environment variables for security in production
  const transporter = nodemailer.createTransport({
    host: 'smtp.gmail.com',
    port: 587,
    secure: false, // use TLS
    auth: {
      user: process.env.GMAIL_USER || 'satishbekkam9999L@gmail.com',
      pass: process.env.GMAIL_PASS || 'vyie kmgx wdye rgyq'
    }
  });

  const mailOptions = {
    from: process.env.GMAIL_USER || 'satishbekkam9999@gmail.com',
    to: 'satishbekkam9999@gmail.com',
    subject: 'PG Hostel Registration',
    text: `\nName: ${name}\nPhone Number: ${mobile}\nAge: ${age}\nSchool/College/Workplace: ${institute}\nCourse/Occupation: ${course}\nAddress: ${address}\nRoom Preference: ${roomType}\nAdditional Information: ${additionalInfo}\n`
  };

  try {
    await transporter.sendMail(mailOptions);
    res.status(200).json({ success: true });
  } catch (err) {
    res.status(500).json({ success: false, error: err.message });
  }
}
