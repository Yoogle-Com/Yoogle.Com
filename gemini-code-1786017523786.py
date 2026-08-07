import os

html_code = """<!DOCTYPE html>
<html lang="hi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Yoogle.com - PACS Automation Services | Yugal Verma</title>
    <!-- Tailwind CSS for Auto-fit Responsive Layout -->
    <script src="https://cdn.tailwindcss.com"></script>
    <!-- FontAwesome Icons -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <!-- Google Analytics GA4 Setup (Placeholder) -->
    <!-- 
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-YOURTRACKINGID"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());
      gtag('config', 'G-YOURTRACKINGID');
    </script>
    -->
    <style>
        .glow-hover:hover {
            box-shadow: 0 10px 25px -5px rgba(37, 99, 235, 0.3);
        }
    </style>
</head>
<body class="bg-slate-50 text-slate-800 font-sans antialiased selection:bg-blue-600 selection:text-white">

    <!-- TOP ANNOUNCEMENT BAR -->
    <div class="bg-gradient-to-r from-blue-900 to-indigo-900 text-white text-xs sm:text-sm py-2 px-4 text-center font-medium shadow-md">
        🚀 <span class="bg-blue-600 px-2 py-0.5 rounded text-xs uppercase tracking-wide mr-1 font-bold">New Version</span> 
        PACS Auto-Tools v2.1 रिलीज़ हो गया है! नीचे दिए गए बटन से डायरेक्ट डाउनलोड करें।
    </div>

    <!-- NAVIGATION BAR -->
    <nav class="bg-white/90 backdrop-blur-md sticky top-0 z-50 border-b border-slate-200">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="flex justify-between h-20 items-center">
                <!-- LOGO SECTION -->
                <div class="flex items-center space-x-3">
                    <div class="w-12 h-12 bg-gradient-to-tr from-blue-700 to-cyan-500 rounded-full flex items-center justify-center text-white font-black text-2xl shadow-lg border-2 border-cyan-300">
                        Y
                    </div>
                    <div>
                        <a href="#" class="text-2xl font-black tracking-tight text-slate-900 flex items-center">
                            Yoogle<span class="text-blue-600">.com</span>
                        </a>
                        <p class="text-xs text-slate-500 font-semibold -mt-1">PACS Automation Solutions</p>
                    </div>
                </div>

                <!-- DESKTOP MENU -->
                <div class="hidden md:flex items-center space-x-8 font-medium text-slate-700 text-sm">
                    <a href="#home" class="hover:text-blue-600 transition">होम</a>
                    <a href="#modules" class="hover:text-blue-600 transition">मॉड्यूल्स</a>
                    <a href="#download" class="hover:text-blue-600 transition">डाउनलोड EXE</a>
                    <a href="#support" class="hover:text-blue-600 transition">सहायता</a>
                    <a href="#contact" class="hover:text-blue-600 transition">संपर्क</a>
                </div>

                <!-- CONTACT HEADER BUTTON -->
                <div class="hidden sm:flex items-center space-x-3">
                    <a href="https://wa.me/916263777500?text=Hello%20Yugal%20Sir,%20mujhe%20Yoogle%20PACS%20Automation%20ke%20bare%20me%20jaankari%20chahiye" target="_blank" class="bg-emerald-600 hover:bg-emerald-700 text-white px-4 py-2.5 rounded-lg font-semibold text-sm flex items-center shadow-md transition">
                        <i class="fa-brands font-bold fa-whatsapp mr-2 text-lg"></i> 6263777500
                    </a>
                </div>
            </div>
        </div>
    </nav>

    <!-- HERO SECTION -->
    <section id="home" class="relative bg-gradient-to-b from-blue-50 via-slate-50 to-white py-16 lg:py-24 overflow-hidden">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="grid grid-cols-1 lg:grid-cols-12 gap-12 items-center">
                
                <div class="lg:col-span-7 text-center lg:text-left space-y-6">
                    <div class="inline-flex items-center space-x-2 bg-blue-100 text-blue-800 text-xs font-bold px-3 py-1.5 rounded-full">
                        <i class="fa-solid fa-bolt text-amber-500"></i>
                        <span>100% सटीक और सुरक्षित ऑटोमेशन टूल</span>
                    </div>

                    <h1 class="text-3xl sm:text-5xl font-black text-slate-900 leading-tight">
                        PACS सेवा समितियों के लिए <br class="hidden sm:inline">
                        <span class="text-transparent bg-clip-text bg-gradient-to-r from-blue-600 to-cyan-600">स्मार्ट वर्क और ऑटोमेशन</span>
                    </h1>

                    <p class="text-slate-600 text-base sm:text-lg max-w-2xl mx-auto lg:mx-0">
                        कार्यालय के काम के दबाव और समय की कमी से मुक्ति पाएं! ERP, PMFBY फसल बीमा और पंजीयक पोर्टल में घंटों का काम मिनटों में 100% शुद्धता के साथ पूरा करें।
                    </p>

                    <!-- OWNER BADGE CARD -->
                    <div class="inline-flex items-center bg-white p-3 rounded-xl border border-slate-200 shadow-sm space-x-3">
                        <div class="w-10 h-10 rounded-full bg-blue-600 text-white font-bold flex items-center justify-center">
                            YV
                        </div>
                        <div class="text-left">
                            <h4 class="font-bold text-slate-800 text-sm">Yugal Verma</h4>
                            <p class="text-xs text-slate-500">Founder & Chief Developer | Mob: 6263777500</p>
                        </div>
                    </div>

                    <!-- CTA BUTTONS -->
                    <div class="flex flex-col sm:flex-row items-center justify-center lg:justify-start gap-4 pt-2">
                        <a href="#download" class="w-full sm:w-auto bg-blue-600 hover:bg-blue-700 text-white font-bold px-8 py-4 rounded-xl shadow-lg shadow-blue-500/30 flex items-center justify-center transition">
                            <i class="fa-solid fa-download mr-3"></i> लेटेस्ट EXE डाउनलोड करें
                        </a>
                        <a href="https://wa.me/916263777500" target="_blank" class="w-full sm:w-auto bg-white hover:bg-slate-100 text-slate-800 border border-slate-300 font-bold px-6 py-4 rounded-xl flex items-center justify-center transition">
                            <i class="fa-brands fa-whatsapp text-emerald-600 mr-2 text-xl"></i> व्हाट्सएप सपोर्ट
                        </a>
                    </div>
                </div>

                <!-- HERO GRAPHIC CARD -->
                <div class="lg:col-span-5">
                    <div class="bg-gradient-to-br from-slate-900 to-blue-950 text-white rounded-3xl p-6 sm:p-8 shadow-2xl border border-slate-800 relative">
                        <div class="flex justify-between items-center border-b border-slate-800 pb-4 mb-6">
                            <div class="flex space-x-2">
                                <div class="w-3 h-3 bg-red-500 rounded-full"></div>
                                <div class="w-3 h-3 bg-amber-500 rounded-full"></div>
                                <div class="w-3 h-3 bg-emerald-500 rounded-full"></div>
                            </div>
                            <span class="text-xs text-blue-400 font-mono">Yoogle_PACS_Suite_v2.1.exe</span>
                        </div>

                        <div class="space-y-4">
                            <div class="bg-slate-800/80 p-4 rounded-xl border border-slate-700/50 flex items-center justify-between">
                                <div class="flex items-center space-x-3">
                                    <i class="fa-solid fa-server text-blue-400 text-xl"></i>
                                    <div>
                                        <h5 class="font-bold text-sm">ERP Bulk Tool</h5>
                                        <p class="text-xs text-slate-400">फास्ट एक्सेल डेटा प्रविष्टि</p>
                                    </div>
                                </div>
                                <span class="bg-emerald-500/20 text-emerald-400 text-xs px-2.5 py-1 rounded-full font-bold">Ready</span>
                            </div>

                            <div class="bg-slate-800/80 p-4 rounded-xl border border-slate-700/50 flex items-center justify-between">
                                <div class="flex items-center space-x-3">
                                    <i class="fa-solid fa-shield-halved text-cyan-400 text-xl"></i>
                                    <div>
                                        <h5 class="font-bold text-sm">PMFBY Insurance Module</h5>
                                        <p class="text-xs text-slate-400">खरीफ / रबी ऑटो-प्रोसेसिंग</p>
                                    </div>
                                </div>
                                <span class="bg-emerald-500/20 text-emerald-400 text-xs px-2.5 py-1 rounded-full font-bold">Active</span>
                            </div>

                            <div class="bg-slate-800/80 p-4 rounded-xl border border-slate-700/50 flex items-center justify-between">
                                <div class="flex items-center space-x-3">
                                    <i class="fa-solid fa-file-signature text-amber-400 text-xl"></i>
                                    <div>
                                        <h5 class="font-bold text-sm">पंजीयक (Panjiyak) Module</h5>
                                        <p class="text-xs text-slate-400">एकीकृत समिति रिकॉर्ड्स</p>
                                    </div>
                                </div>
                                <span class="bg-emerald-500/20 text-emerald-400 text-xs px-2.5 py-1 rounded-full font-bold">Active</span>
                            </div>
                        </div>

                        <div class="mt-6 pt-4 border-t border-slate-800 flex justify-between items-center text-xs text-slate-400">
                            <span><i class="fa-solid fa-circle text-emerald-500 text-[8px] mr-1"></i> Auto-Update Engine On</span>
                            <span>Windows 10/11 Compatible</span>
                        </div>
                    </div>
                </div>

            </div>
        </div>
    </section>

    <!-- MODULES SECTION -->
    <section id="modules" class="py-16 bg-white">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="text-center max-w-3xl mx-auto mb-16">
                <h2 class="text-3xl font-black text-slate-900 mb-4">हमारे स्मार्ट ऑटोमेशन मॉड्यूल्स</h2>
                <p class="text-slate-600">समिति के रोजमर्रा के ऑनलाइन और डेटा प्रविष्टि कार्यों को आसान बनाने के लिए खास टूल्स।</p>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
                
                <!-- MODULE 1 -->
                <div class="bg-slate-50 border border-slate-200 rounded-2xl p-8 hover:border-blue-500 transition glow-hover flex flex-col justify-between">
                    <div>
                        <div class="w-14 h-14 bg-blue-600 text-white rounded-2xl flex items-center justify-center text-2xl mb-6 shadow-lg shadow-blue-500/20">
                            <i class="fa-solid fa-database"></i>
                        </div>
                        <h3 class="text-xl font-bold text-slate-900 mb-3">ERP Automation Tool</h3>
                        <p class="text-slate-600 text-sm leading-relaxed mb-6">
                            ERP पोर्टल पर घंटों लगने वाली एंट्रीज को Excel Sheet के माध्यम से बल्क में ऑटोमैटिकली पूरा करें। काम में 100% सटीकता।
                        </p>
                        <ul class="space-y-2 text-xs font-semibold text-slate-700 mb-6">
                            <li class="flex items-center"><i class="fa-solid fa-check text-emerald-500 mr-2"></i> बल्क डेटा अपलोड सुविधा</li>
                            <li class="flex items-center"><i class="fa-solid fa-check text-emerald-500 mr-2"></i> समय एवं श्रम की भारी बचत</li>
                            <li class="flex items-center"><i class="fa-solid fa-check text-emerald-500 mr-2"></i> मानवीय भूलों से मुक्ति</li>
                        </ul>
                    </div>
                    <a href="https://wa.me/916263777500?text=ERP%20Module%20ki%20jaankari" class="text-blue-600 font-bold text-sm hover:underline flex items-center">
                        अधिक जानकारी <i class="fa-solid fa-arrow-right ml-2 text-xs"></i>
                    </a>
                </div>

                <!-- MODULE 2 -->
                <div class="bg-slate-50 border border-slate-200 rounded-2xl p-8 hover:border-blue-500 transition glow-hover flex flex-col justify-between">
                    <div>
                        <div class="w-14 h-14 bg-cyan-600 text-white rounded-2xl flex items-center justify-center text-2xl mb-6 shadow-lg shadow-cyan-500/20">
                            <i class="fa-solid fa-shield-heart"></i>
                        </div>
                        <h3 class="text-xl font-bold text-slate-900 mb-3">PMFBY Insurance Module</h3>
                        <p class="text-slate-600 text-sm leading-relaxed mb-6">
                            प्रधानमंत्री फसल बीमा योजना पोर्टल पर फसल बीमा प्रीमियम और किसानों की जानकारी बिना किसी रुकावट के बल्क में सबमिट करें।
                        </p>
                        <ul class="space-y-2 text-xs font-semibold text-slate-700 mb-6">
                            <li class="flex items-center"><i class="fa-solid fa-check text-emerald-500 mr-2"></i> खरीफ और रबी पोर्टल सपोर्ट</li>
                            <li class="flex items-center"><i class="fa-solid fa-check text-emerald-500 mr-2"></i> ऑटोमैटिक फील्ड मैपिंग</li>
                            <li class="flex items-center"><i class="fa-solid fa-check text-emerald-500 mr-2"></i> त्वरित एरर चेकिंग</li>
                        </ul>
                    </div>
                    <a href="https://wa.me/916263777500?text=PMFBY%20Module%20ki%20jaankari" class="text-blue-600 font-bold text-sm hover:underline flex items-center">
                        अधिक जानकारी <i class="fa-solid fa-arrow-right ml-2 text-xs"></i>
                    </a>
                </div>

                <!-- MODULE 3 -->
                <div class="bg-slate-50 border border-slate-200 rounded-2xl p-8 hover:border-blue-500 transition glow-hover flex flex-col justify-between">
                    <div>
                        <div class="w-14 h-14 bg-indigo-600 text-white rounded-2xl flex items-center justify-center text-2xl mb-6 shadow-lg shadow-indigo-500/20">
                            <i class="fa-solid fa-id-card"></i>
                        </div>
                        <h3 class="text-xl font-bold text-slate-900 mb-3">पंजीयक (Panjiyak) Module</h3>
                        <p class="text-slate-600 text-sm leading-relaxed mb-6">
                            पंजीयक संस्थाएं और सहकारिता विभाग के मॉड्यूल पर एंट्रीज एवं रिपोर्ट तैयार करने का सबसे तेज़ और भरोसेमंद समाधान।
                        </p>
                        <ul class="space-y-2 text-xs font-semibold text-slate-700 mb-6">
                            <li class="flex items-center"><i class="fa-solid fa-check text-emerald-500 mr-2"></i> एकीकृत किसान डेटा ऑटोमेशन</li>
                            <li class="flex items-center"><i class="fa-solid fa-check text-emerald-500 mr-2"></i> वन-क्लिक डेटा सत्यापन</li>
                            <li class="flex items-center"><i class="fa-solid fa-check text-emerald-500 mr-2"></i> नियमों के पूर्ण अनुकूल</li>
                        </ul>
                    </div>
                    <a href="https://wa.me/916263777500?text=Panjiyak%20Module%20ki%20jaankari" class="text-blue-600 font-bold text-sm hover:underline flex items-center">
                        अधिक जानकारी <i class="fa-solid fa-arrow-right ml-2 text-xs"></i>
                    </a>
                </div>

            </div>
        </div>
    </section>

    <!-- DOWNLOAD & EXE RELEASES SECTION -->
    <section id="download" class="py-16 bg-slate-900 text-white">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="bg-gradient-to-r from-blue-900/50 to-indigo-900/50 rounded-3xl p-8 sm:p-12 border border-slate-800 text-center max-w-4xl mx-auto">
                
                <span class="bg-blue-600/30 text-blue-400 font-bold text-xs uppercase px-4 py-1.5 rounded-full border border-blue-500/30">Official Download Center</span>
                
                <h2 class="text-3xl sm:text-4xl font-black mt-4 mb-4">लेटेस्ट Yoogle EXE टूल डाउनलोड करें</h2>
                <p class="text-slate-300 text-sm sm:text-base max-w-2xl mx-auto mb-8">
                    नीचे दिए गए बटन से आप हमेशा नवीनतम वर्शन डाउनलोड कर सकते हैं। यह टूल सीधे GitHub Release सर्वर से जुड़ा हुआ है।
                </p>

                <!-- DIRECT EXE DOWNLOAD LINK CONNECTED TO GITHUB RELEASES -->
                <div class="inline-block">
                    <a href="https://github.com/yugalverma/pacs-automation/releases/latest/download/Yoogle_PACS_Suite.exe" class="bg-blue-600 hover:bg-blue-500 text-white font-black text-lg px-8 py-5 rounded-2xl shadow-xl shadow-blue-600/40 inline-flex items-center transition transform hover:-translate-y-0.5">
                        <i class="fa-solid fa-download mr-3 text-2xl"></i>
                        <span>Download Yoogle_PACS_Suite.exe (Latest)</span>
                    </a>
                </div>

                <div class="grid grid-cols-1 sm:grid-cols-3 gap-4 mt-10 pt-8 border-t border-slate-800/80 text-xs text-slate-400">
                    <div><i class="fa-solid fa-shield text-emerald-400 mr-1"></i> 100% Virus Free & Tested</div>
                    <div><i class="fa-solid fa-arrows-rotate text-blue-400 mr-1"></i> Auto-Update Supported</div>
                    <div><i class="fa-solid fa-key text-amber-400 mr-1"></i> License Key Required on First Run</div>
                </div>

            </div>
        </div>
    </section>

    <!-- USER REGISTRATION / INQUIRY FORM (KNOW WHO VISITED) -->
    <section id="contact" class="py-16 bg-slate-50">
        <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="bg-white rounded-3xl p-8 sm:p-12 border border-slate-200 shadow-xl">
                <div class="text-center mb-8">
                    <h2 class="text-2xl sm:text-3xl font-black text-slate-900">सॉफ्टवेयर डेमो एवं लाइसेंस इंक्वायरी</h2>
                    <p class="text-slate-600 text-sm mt-2">अपना विवरण दर्ज करें, हमारी टीम आपको तुरंत संपर्क करके सॉफ्टवेयर चलाना सिखाएगी।</p>
                </div>

                <!-- FORM CONNECTED TO GOOGLE FORMS OR CUSTOM WEBHOOK -->
                <form action="https://formspree.io/f/moqvgpza" method="POST" class="space-y-6">
                    <div class="grid grid-cols-1 sm:grid-cols-2 gap-6">
                        <div>
                            <label class="block text-xs font-bold uppercase text-slate-700 mb-2">आपका नाम</label>
                            <input type="text" name="name" required placeholder="जैसे: युगल वर्मा" class="w-full px-4 py-3 rounded-xl border border-slate-300 focus:ring-2 focus:ring-blue-600 focus:outline-none text-sm">
                        </div>
                        <div>
                            <label class="block text-xs font-bold uppercase text-slate-700 mb-2">मोबाइल नंबर (WhatsApp)</label>
                            <input type="tel" name="phone" required placeholder="6263777500" class="w-full px-4 py-3 rounded-xl border border-slate-300 focus:ring-2 focus:ring-blue-600 focus:outline-none text-sm">
                        </div>
                    </div>

                    <div class="grid grid-cols-1 sm:grid-cols-2 gap-6">
                        <div>
                            <label class="block text-xs font-bold uppercase text-slate-700 mb-2">समिति / संस्था का नाम</label>
                            <input type="text" name="pacs_name" placeholder="जैसे: सेवा सहकारी समिति विरेंद्रनगर" class="w-full px-4 py-3 rounded-xl border border-slate-300 focus:ring-2 focus:ring-blue-600 focus:outline-none text-sm">
                        </div>
                        <div>
                            <label class="block text-xs font-bold uppercase text-slate-700 mb-2">ज़िला / क्षेत्र</label>
                            <input type="text" name="district" placeholder="जैसे: कबीरधाम / रायपुर" class="w-full px-4 py-3 rounded-xl border border-slate-300 focus:ring-2 focus:ring-blue-600 focus:outline-none text-sm">
                        </div>
                    </div>

                    <div>
                        <label class="block text-xs font-bold uppercase text-slate-700 mb-2">आवश्यक मॉड्यूल चुनिए</label>
                        <select name="required_module" class="w-full px-4 py-3 rounded-xl border border-slate-300 focus:ring-2 focus:ring-blue-600 focus:outline-none text-sm">
                            <option>ERP Automation Tool</option>
                            <option>PMFBY Insurance Module</option>
                            <option>Panjiyak Module</option>
                            <option>सभी मॉड्यूल्स (Combo)</option>
                        </select>
                    </div>

                    <button type="submit" class="w-full bg-slate-900 hover:bg-slate-800 text-white font-bold py-4 rounded-xl shadow-lg transition text-sm uppercase tracking-wider">
                        सबमिट करें & रजिस्ट्रेशन प्राप्त करें
                    </button>
                </form>
            </div>
        </div>
    </section>

    <!-- FOOTER SECTION -->
    <footer class="bg-slate-950 text-slate-400 py-12 border-t border-slate-800">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center sm:text-left">
            <div class="grid grid-cols-1 md:grid-cols-3 gap-8 mb-8">
                <div>
                    <h3 class="text-white text-xl font-bold mb-2">Yoogle.com</h3>
                    <p class="text-xs text-slate-500 leading-relaxed">
                        छत्तीसगढ़ एवं अन्य राज्यों की सेवा सहकारी समितियों (PACS) के लिए सर्वश्रेष्ठ ऑटोमेशन और सॉफ्टवेयर समाधान।
                    </p>
                </div>
                <div>
                    <h4 class="text-white font-bold text-sm mb-3">संपर्क सूत्र</h4>
                    <p class="text-xs mb-1"><i class="fa-solid fa-user text-blue-500 mr-2"></i> Yugal Verma</p>
                    <p class="text-xs mb-1"><i class="fa-solid fa-phone text-blue-500 mr-2"></i> Mob: 6263777500</p>
                    <p class="text-xs"><i class="fa-solid fa-globe text-blue-500 mr-2"></i> www.Yoogle.com</p>
                </div>
                <div>
                    <h4 class="text-white font-bold text-sm mb-3">व्हाट्सएप ग्रुप से जुड़ें</h4>
                    <p class="text-xs text-slate-500 mb-3">समय-समय पर अपडेट्स और नई ट्रिक पाने के लिए ग्रुप ज्वाइन करें:</p>
                    <a href="https://wa.me/916263777500" target="_blank" class="inline-flex items-center bg-emerald-600 text-white px-4 py-2 rounded-lg text-xs font-bold">
                        <i class="fa-brands fa-whatsapp mr-2 text-sm"></i> WhatsApp Group Join
                    </a>
                </div>
            </div>

            <div class="pt-8 border-t border-slate-900 text-center text-xs text-slate-600">
                © 2026 Yoogle.com Automation Services. सर्वाधिकार सुरक्षित। Designed for Yugal Verma.
            </div>
        </div>
    </footer>

    <!-- FLOATING WHATSAPP BUTTON (FOR MOBILE & LAPTOP) -->
    <a href="https://wa.me/916263777500?text=Namaste%20Yugal%20Sir" target="_blank" class="fixed bottom-6 right-6 bg-emerald-500 text-white w-14 h-14 rounded-full flex items-center justify-center text-3xl shadow-2xl hover:bg-emerald-600 transition z-50">
        <i class="fa-brands fa-whatsapp"></i>
    </a>

</body>
</html>
"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_code)

print("HTML index.html file generated successfully.")