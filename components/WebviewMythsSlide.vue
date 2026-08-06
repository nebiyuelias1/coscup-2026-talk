<template>
  <div class="webview-myths-slide w-full my-auto flex flex-col justify-center">
    <!-- Header -->
    <div class="flex justify-between items-center mb-2">
      <span class="rails-badge font-bold">🗣️ Tech Industry Dogma</span>
      <span class="text-xs font-mono text-slate-400">Conventional Wisdom vs Reality</span>
    </div>

    <h2 class="text-3xl font-black tracking-tight text-white mb-4 text-center">
      Then The "Cool Kids" <span class="text-red-500">Speak Up... 🙄</span>
    </h2>

    <!-- Centered Hero Image Frame with Overlays -->
    <div class="max-w-2xl mx-auto w-full my-2">
      <div class="bg-slate-900 border-2 border-purple-500/40 rounded-2xl p-2.5 shadow-2xl relative overflow-hidden group">
        <div class="rounded-xl overflow-hidden border border-slate-800 bg-black relative">
          <img 
            src="/mean_girls.png" 
            alt="Mean Girls Judging Movie Still" 
            class="w-full h-72 object-cover rounded-lg transform transition-transform group-hover:scale-[1.01]"
          />

          <!-- Speech Bubble Overlay -->
          <div class="absolute top-3 left-1/2 -translate-x-1/2 bg-slate-950/95 border-2 border-pink-500/80 backdrop-blur-md px-4 py-2 rounded-2xl shadow-2xl text-center z-20">
            <span class="text-xs md:text-sm font-bold text-pink-300 flex items-center gap-1.5 font-sans">
              💬 <em>"Eww... a WebView? You can't deploy with us!"</em> 💅
            </span>
          </div>

          <!-- Character Role Badges -->
          <!-- Karen (Left) -->
          <div class="absolute bottom-3 left-3 bg-slate-950/90 border border-purple-500/70 backdrop-blur-md px-2.5 py-1 rounded-lg text-xs font-mono text-purple-300 z-10 font-bold shadow-lg">
            💅 Tech Twitter
          </div>

          <!-- Regina George (Center) -->
          <div class="absolute bottom-3 left-1/2 -translate-x-1/2 bg-pink-950/90 border-2 border-pink-400/80 backdrop-blur-md px-3 py-1 rounded-lg text-xs font-mono text-pink-200 z-10 font-bold shadow-xl">
            👑 Senior RN Architect
          </div>

          <!-- Gretchen (Right) -->
          <div class="absolute bottom-3 right-3 bg-slate-950/90 border border-purple-500/70 backdrop-blur-md px-2.5 py-1 rounded-lg text-xs font-mono text-purple-300 z-10 font-bold shadow-lg">
            📦 SPA Purist
          </div>
        </div>
      </div>

      <div class="text-xs font-mono text-purple-300 flex items-center justify-between px-2 mt-2">
        <span>🎬 Mean Girls (2004)</span>
        <span class="text-slate-400">Mobile Dev Community Dogma</span>
      </div>
    </div>

  </div>
</template>

<script setup>
</script>
