export default function AaraDanceStudioPage() {
  const classes = [
    {
      title: "Tiny Stars (5–8)",
      level: "Beginner / Intermediate",
      days: "Wednesday & Friday",
      time: "6:30 PM – 7:30 PM",
      pricing: "$60/month (4 classes) | $100/month (8 classes)",
    },
    {
      title: "Shining Stars (9+)",
      level: "Beginner / Intermediate",
      days: "Tuesday",
      time: "7:00 PM – 8:00 PM",
      pricing: "$60/month (4 classes) | $100/month (8 classes)",
    },
    {
      title: "Dream Chasers (Ladies 18+)",
      level: "Beginner / Intermediate",
      days: "Thursday & Saturday",
      time: "Thu 6:30 PM – 7:30 PM | Sat 10:30 AM – 11:30 AM",
      pricing: "$60/month (4 classes) | $90/month (8 classes)",
    },
  ];

  const danceStyles = [
    "Bollywood",
    "Kollywood",
    "Tollywood",
    "Semi-Classical",
    "Freestyle",
    "Hip Hop",
    "Kuthu",
  ];

  return (
    <div className="min-h-screen bg-black text-white font-sans">
      {/* Hero Section */}
      <section className="relative overflow-hidden border-b border-yellow-600">
        <div className="absolute inset-0 bg-gradient-to-b from-yellow-900/20 via-black to-black"></div>

        <div className="relative max-w-7xl mx-auto px-6 py-16 grid md:grid-cols-2 gap-10 items-center">
          <div>
            <img
              src="/images/AARALOGO_Final.PNG"
              alt="AARA Dance Studio"
              className="w-64 mb-6 rounded-3xl shadow-2xl border border-yellow-500"
            />

            <h1 className="text-5xl md:text-6xl font-bold leading-tight text-yellow-400">
              AARA Dance Studio
            </h1>

            <p className="text-xl text-gray-300 mt-3 tracking-wide">
              ADS – Dallas
            </p>

            <p className="mt-6 text-lg text-gray-200 leading-relaxed">
              Where Passion Meets Performance ✨
            </p>

            <div className="mt-8 bg-gradient-to-r from-yellow-600 to-yellow-400 text-black rounded-2xl p-5 shadow-2xl">
              <h2 className="text-2xl font-bold">🎉 Early Bird Offer</h2>
              <p className="mt-2 text-lg font-semibold">
                First 10 registrations get ONLY $50/month for the first 2 months.
              </p>
              <p className="mt-1 text-sm">
                Regular pricing applies starting from the 11th registration.
              </p>
            </div>
          </div>

          <div className="grid grid-cols-2 gap-4">
            <img
              src="/images/MAH00221_Original.jpeg"
              className="rounded-3xl object-cover h-80 w-full border border-gray-600 shadow-xl"
            />
            <img
              src="/images/IMG_6427.JPG"
              className="rounded-3xl object-cover h-80 w-full border border-yellow-500 shadow-xl"
            />
            <img
              src="/images/IMG_7413.jpeg"
              className="rounded-3xl object-cover h-72 w-full border border-gray-600 shadow-xl"
            />
            <img
              src="/images/IMG_6917.jpeg"
              className="rounded-3xl object-cover h-72 w-full border border-yellow-500 shadow-xl"
            />
          </div>
        </div>
      </section>

      {/* About Section */}
      <section className="max-w-7xl mx-auto px-6 py-16">
        <div className="bg-zinc-900 rounded-3xl p-8 border border-yellow-600 shadow-2xl">
          <h2 className="text-4xl font-bold text-yellow-400 mb-6">
            Find Your Groove!
          </h2>

          <p className="text-gray-300 text-lg leading-relaxed mb-8">
            At AARA Dance Studio, we inspire students of all ages to build confidence,
            creativity, rhythm, and stage presence through energetic and expressive dance training.
          </p>

          <div className="grid md:grid-cols-2 gap-6 text-gray-200">
            <div className="bg-black/50 p-5 rounded-2xl border border-gray-700">
              <h3 className="text-yellow-400 text-xl font-bold mb-2">Bollywood</h3>
              <p>A fun and energetic dance style inspired by Hindi movie songs and Indian cinema.</p>
            </div>

            <div className="bg-black/50 p-5 rounded-2xl border border-gray-700">
              <h3 className="text-yellow-400 text-xl font-bold mb-2">Kollywood</h3>
              <p>A vibrant dance form based on Tamil movie music, known for expressive moves and powerful energy.</p>
            </div>

            <div className="bg-black/50 p-5 rounded-2xl border border-gray-700">
              <h3 className="text-yellow-400 text-xl font-bold mb-2">Tollywood</h3>
              <p>A lively dance style inspired by Telugu film songs, featuring fast beats and dynamic choreography.</p>
            </div>

            <div className="bg-black/50 p-5 rounded-2xl border border-gray-700">
              <h3 className="text-yellow-400 text-xl font-bold mb-2">Semi-Classical</h3>
              <p>A graceful blend of classical Indian dance techniques with modern expressions and music.</p>
            </div>

            <div className="bg-black/50 p-5 rounded-2xl border border-gray-700">
              <h3 className="text-yellow-400 text-xl font-bold mb-2">Freestyle</h3>
              <p>A creative dance form that allows dancers to move freely and express themselves without fixed rules.</p>
            </div>

            <div className="bg-black/50 p-5 rounded-2xl border border-gray-700">
              <h3 className="text-yellow-400 text-xl font-bold mb-2">Hip Hop</h3>
              <p>A trendy and energetic street dance style with sharp movements, rhythm, and attitude.</p>
            </div>

            <div className="bg-black/50 p-5 rounded-2xl border border-gray-700 md:col-span-2">
              <h3 className="text-yellow-400 text-xl font-bold mb-2">Kuthu</h3>
              <p>A high-energy South Indian folk-inspired dance style known for its fun beats and energetic moves.</p>
            </div>
          </div>
        </div>
      </section>

      {/* Instructor Section */}
      <section className="max-w-7xl mx-auto px-6 pb-16">
        <div className="bg-gradient-to-r from-zinc-900 to-black border border-yellow-600 rounded-3xl p-8 shadow-2xl">
          <h2 className="text-4xl font-bold text-yellow-400 mb-6">Dance Instructors</h2>

          <div className="grid md:grid-cols-2 gap-8 items-center">
            <div>
              <img
                src="/images/MAH00221_Original.jpeg"
                className="rounded-3xl shadow-2xl border border-yellow-500"
              />
            </div>

            <div>
              <h3 className="text-3xl font-bold text-white">Rekha Mahendran</h3>
              <p className="text-gray-300 mt-2 text-lg">
                Passionate dance instructor dedicated to helping students express themselves through movement,
                creativity, and confidence.
              </p>

              <div className="mt-8">
                <h3 className="text-3xl font-bold text-white">Mahendran Ramachandran</h3>
                <p className="text-gray-300 mt-2 text-lg">
                  Inspiring dancers with energetic choreography, performance techniques, and dynamic stage presence.
                </p>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Classes */}
      <section className="max-w-7xl mx-auto px-6 pb-16">
        <h2 className="text-4xl font-bold text-center text-yellow-400 mb-10">
          Class Programs
        </h2>

        <div className="grid md:grid-cols-3 gap-8">
          {classes.map((item, index) => (
            <div
              key={index}
              className="bg-zinc-900 border border-yellow-600 rounded-3xl p-6 shadow-2xl hover:scale-105 transition-all duration-300"
            >
              <h3 className="text-2xl font-bold text-yellow-400 mb-3">
                {item.title}
              </h3>

              <p className="text-gray-300 mb-2">{item.level}</p>
              <p className="text-white font-semibold">{item.days}</p>
              <p className="text-gray-300 mt-2">{item.time}</p>

              <div className="mt-6 bg-black rounded-2xl p-4 border border-gray-700">
                <p className="text-yellow-300 font-semibold">{item.pricing}</p>
              </div>
            </div>
          ))}
        </div>
      </section>

      {/* Registration Form */}
      <section className="max-w-5xl mx-auto px-6 pb-20">
        <div className="bg-zinc-900 border border-yellow-600 rounded-3xl p-8 shadow-2xl">
          <h2 className="text-4xl font-bold text-yellow-400 mb-8 text-center">
            Student Registration
          </h2>

          <form className="grid md:grid-cols-2 gap-6">
            <input type="text" placeholder="Student Name" className="bg-black border border-gray-700 rounded-xl p-4" />
            <input type="text" placeholder="Date of Birth / Age" className="bg-black border border-gray-700 rounded-xl p-4" />
            <input type="text" placeholder="Parent / Guardian Name" className="bg-black border border-gray-700 rounded-xl p-4" />
            <input type="tel" placeholder="Phone Number" className="bg-black border border-gray-700 rounded-xl p-4" />
            <input type="email" placeholder="Email Address" className="bg-black border border-gray-700 rounded-xl p-4" />
            <select className="bg-black border border-gray-700 rounded-xl p-4">
              <option>Select Class Program</option>
              <option>Tiny Stars</option>
              <option>Shining Stars</option>
              <option>Dream Chasers</option>
            </select>

            <select className="bg-black border border-gray-700 rounded-xl p-4">
              <option>Preferred Dance Style</option>
              {danceStyles.map((style) => (
                <option key={style}>{style}</option>
              ))}
            </select>

            <select className="bg-black border border-gray-700 rounded-xl p-4">
              <option>Select Package</option>
              <option>4 Classes / Month</option>
              <option>8 Classes / Month</option>
            </select>

            <textarea
              placeholder="Medical Information / Notes"
              className="md:col-span-2 bg-black border border-gray-700 rounded-xl p-4 min-h-[120px]"
            ></textarea>

            <div className="md:col-span-2 flex items-center gap-3 text-gray-300">
              <input type="checkbox" className="w-5 h-5" />
              <p>
                I consent to photo/video usage for studio events and promotions.
              </p>
            </div>

            <div className="md:col-span-2 bg-black rounded-2xl border border-yellow-500 p-5">
              <h3 className="text-2xl font-bold text-yellow-400 mb-3">
                Zelle Payment
              </h3>
              <p className="text-lg text-white">+1 (631) 836-7972</p>
              <p className="text-gray-400 mt-2">
                Please complete your Zelle payment after submitting the registration form.
              </p>
            </div>

            <button className="md:col-span-2 bg-gradient-to-r from-yellow-500 to-yellow-300 text-black text-xl font-bold py-4 rounded-2xl hover:scale-105 transition-all duration-300 shadow-2xl">
              Submit Registration
            </button>
          </form>
        </div>
      </section>

      {/* Footer */}
      <footer className="border-t border-yellow-700 py-10 text-center text-gray-400">
        <p className="text-xl text-yellow-400 font-semibold">
          AARA Dance Studio – ADS Dallas
        </p>
        <p className="mt-2">Where Passion Meets Performance ✨</p>
      </footer>
    </div>
  );
}
