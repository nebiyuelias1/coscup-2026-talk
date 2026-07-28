<template>
  <div class="flex flex-col items-center justify-center h-auto my-auto px-4 text-center relative z-10 py-2">

    <!-- Top Badges -->
    <div class="flex items-center gap-2 mb-3">
      <span class="rails-badge">⚡ Portfolio & Talks</span>
      <div class="px-3 py-1 rounded-full text-xs font-mono font-bold bg-slate-900 text-slate-300 border border-slate-700 flex items-center gap-2">
        <img src="/coscup_logo.png" alt="COSCUP Logo" class="h-4 object-contain" />
        <span>2026</span>
      </div>
    </div>

    <!-- Slide Title -->
    <h1 class="text-3xl font-extrabold tracking-tight mb-1">
      Scan for Slides, Code & More Talks
    </h1>
    
    <p class="text-slate-300 text-xs max-w-xl mx-auto mb-4">
      Scan the QR code below or visit <a href="https://netale.et/#talks" target="_blank" class="text-red-400 hover:text-red-300 font-mono font-bold underline">netale.et/#talks</a> to access full presentation resources.
    </p>

    <!-- Main Card with QR Code and Highlights -->
    <div class="bg-slate-900/90 border border-red-500/40 rounded-2xl p-4 max-w-2xl w-full shadow-2xl backdrop-blur-md text-left">
      <div class="grid grid-cols-1 md:grid-cols-5 gap-5 items-center">

        <!-- Left: QR Code Display -->
        <div class="md:col-span-2 flex flex-col items-center justify-center bg-slate-950 p-3 rounded-xl border border-slate-800 text-center">
          <div class="w-32 h-32 bg-white p-2 rounded-xl shadow-xl flex items-center justify-center">
            <!-- Precise Scannable SVG QR Code for https://netale.et/#talks -->
            <svg class="w-full h-full text-slate-950" viewBox="0 0 33 33" shape-rendering="crispEdges">
              <path fill="#ffffff" d="M0 0h33v33H0z"/>
              <path stroke="#000000" d="M4 4.5h7m6 0h1m4 0h7M4 5.5h1m5 0h1m5 0h4m2 0h1m5 0h1M4 6.5h1m1 0h3m1 0h1m1 0h1m1 0h1m3 0h3m1 0h1m1 0h3m1 0h1M4 7.5h1m1 0h3m1 0h1m1 0h1m4 0h1m1 0h2m1 0h1m1 0h3m1 0h1M4 8.5h1m1 0h3m1 0h1m1 0h5m3 0h1m1 0h1m1 0h3m1 0h1M4 9.5h1m5 0h1m1 0h2m3 0h1m1 0h2m1 0h1m5 0h1M4 10.5h7m1 0h1m1 0h1m1 0h1m1 0h1m1 0h1m1 0h7M12 11.5h1m2 0h1m2 0h3M4 12.5h1m1 0h5m2 0h2m2 0h3m2 0h5M5 13.5h1m1 0h1m1 0h1m2 0h1m3 0h1m1 0h1m1 0h1m2 0h1m3 0h1M5 14.5h4m1 0h1m1 0h1m5 0h2m1 0h2m1 0h2m1 0h2M4 15.5h3m2 0h1m1 0h1m8 0h5m3 0h1M4 16.5h1m1 0h2m1 0h6m2 0h2m2 0h2m1 0h1m1 0h3M4 17.5h1m1 0h1m1 0h1m2 0h1m1 0h2m1 0h1m4 0h1m1 0h1m1 0h1m1 0h1M4 18.5h1m1 0h1m1 0h1m1 0h2m7 0h7m1 0h2M4 19.5h1m1 0h1m1 0h2m1 0h2m3 0h1m1 0h3m1 0h3m3 0h1M4 20.5h1m1 0h3m1 0h2m1 0h1m2 0h9m1 0h1M12 21.5h2m3 0h1m1 0h2m3 0h2M4 22.5h7m4 0h2m1 0h1m1 0h1m1 0h1m1 0h1m1 0h3M4 23.5h1m5 0h1m1 0h1m2 0h1m4 0h1m3 0h2m2 0h1M4 24.5h1m1 0h3m1 0h1m1 0h2m1 0h10m1 0h1M4 25.5h1m1 0h3m1 0h1m1 0h2m2 0h2m1 0h1m1 0h2m1 0h5M4 26.5h1m1 0h3m1 0h1m1 0h1m4 0h1m2 0h1m4 0h2m1 0h1M4 27.5h1m5 0h1m2 0h4m1 0h3m1 0h4m2 0h1M4 28.5h7m1 0h1m1 0h1m2 0h2m2 0h8"/>
            </svg>
          </div>
          <div class="text-xs text-amber-300 font-mono font-bold mt-2.5">
            netale.et/#talks
          </div>
        </div>

        <!-- Right: Links & Content Info -->
        <div class="md:col-span-3 space-y-3">
          <div class="flex items-center gap-3">
            <div class="w-11 h-11 rounded-xl bg-gradient-to-tr from-red-600 to-amber-500 p-0.5 shadow shrink-0 overflow-hidden">
              <img src="/nebiyu.png" alt="Nebiyu Elias Talefe" class="w-full h-full object-cover object-top rounded-[10px]" />
            </div>
            <div>
              <h3 class="text-base font-black text-white m-0">
                Neba's Portfolio 🇪🇹
              </h3>
              <p class="text-xs text-red-400 font-semibold m-0 mt-0.5">
                https://netale.et/#talks
              </p>
            </div>
          </div>

          <ul class="text-xs text-slate-300 space-y-2 m-0 p-0 list-none">
            <li class="flex items-center gap-2">
              <span class="text-red-400 font-bold">▶</span>
              <span><strong>Talk Slides:</strong> COSCUP 2026 Hotwire Native deck</span>
            </li>
            <li class="flex items-center gap-2">
              <span class="text-amber-400 font-bold">▶</span>
              <span><strong>Code Repos:</strong> Starter templates & open-source tools</span>
            </li>
            <li class="flex items-center gap-2">
              <span class="text-emerald-400 font-bold">▶</span>
              <span><strong>Upcoming Events:</strong> Conference & meetup schedules</span>
            </li>
          </ul>

          <div class="pt-2">
            <a 
              href="https://netale.et/#talks" 
              target="_blank" 
              class="inline-flex items-center gap-2 px-4 py-2 bg-gradient-to-r from-red-600 to-amber-500 hover:from-red-500 hover:to-amber-400 text-white text-xs font-bold rounded-xl shadow-lg transition"
            >
              <span>🌐 Open Portfolio Talk Section</span>
              <span>→</span>
            </a>
          </div>
        </div>

      </div>
    </div>

  </div>
</template>

<script setup>
</script>
