<template>
  <div class="idea-to-reality-slide w-full my-auto flex flex-col justify-center text-left">
    
    <!-- Header Badge -->
    <div class="flex justify-between items-center mb-2">
      <span class="rails-badge font-bold">💡 The Genesis</span>
      <span class="text-xs font-mono text-slate-400">0 to 1 Transformation</span>
    </div>

    <!-- Main Title -->
    <h2 class="text-3xl font-black tracking-tight text-white mb-6">
      Turning an <span class="text-amber-400">Idea</span> into <span class="text-emerald-400">Production Reality 🚀</span>
    </h2>

    <!-- Graphic Transformation Pipeline -->
    <div class="relative bg-slate-900/90 border border-red-500/40 rounded-2xl p-6 shadow-2xl backdrop-blur-md mb-5 overflow-hidden">
      
      <!-- Background Ambient Glows -->
      <div class="absolute -top-12 -left-12 w-40 h-40 bg-amber-500/10 rounded-full blur-3xl pointer-events-none"></div>
      <div class="absolute -bottom-12 -right-12 w-40 h-40 bg-emerald-500/15 rounded-full blur-3xl pointer-events-none"></div>

      <div class="grid grid-cols-1 md:grid-cols-11 gap-3 items-center relative z-10">
        
        <!-- Node 1: Raw Idea (Napkin Sketch) [Cols 1-4] -->
        <div class="md:col-span-4 bg-slate-950/90 border-2 border-amber-500/40 rounded-xl p-4 space-y-3 shadow-xl relative group">
          <div class="flex items-center justify-between">
            <span class="text-[10px] font-mono font-bold text-amber-400 bg-amber-950/80 px-2 py-0.5 rounded border border-amber-800">
              01. Raw Idea
            </span>
            <span class="text-2xl animate-pulse">💡</span>
          </div>
          
          <!-- Wireframe Mockup Card -->
          <div class="border border-dashed border-slate-700 rounded-lg p-2.5 bg-slate-900/60 space-y-1.5 font-mono text-[11px]">
            <div class="h-2 w-2/3 bg-amber-500/40 rounded"></div>
            <div class="h-2 w-full bg-slate-800 rounded"></div>
            <div class="h-2 w-4/5 bg-slate-800 rounded"></div>
            <div class="pt-1 flex gap-1">
              <div class="h-3 w-10 bg-amber-500/30 rounded border border-amber-500/40"></div>
              <div class="h-3 w-10 bg-slate-800 rounded"></div>
            </div>
          </div>

          <div class="text-xs text-slate-300 font-medium">
            Napkin sketch & feature vision
          </div>
        </div>

        <!-- Connection Arrow / Larger Rails Engine Core [Cols 5-7] -->
        <div class="md:col-span-3 flex flex-col items-center justify-center text-center py-2 relative">
          <!-- Animated Connecting Line & Gem Badge -->
          <div class="hidden md:flex items-center w-full relative">
            <div class="h-0.5 bg-gradient-to-r from-amber-500 via-red-500 to-emerald-500 w-full"></div>
            <div class="absolute inset-0 flex items-center justify-center">
              <div class="bg-red-950 border-2 border-red-500 text-red-200 px-4 py-2 rounded-full font-mono text-sm font-black shadow-2xl flex items-center gap-2">
                <img src="/ruby_taiwan_logo.svg" alt="Rails Logo" class="h-7 w-7 object-contain drop-shadow" />
                <span>Rails</span>
              </div>
            </div>
          </div>
        </div>

        <!-- Node 2: Majestic Production Web App [Cols 8-11] -->
        <div class="md:col-span-4 bg-slate-950/95 border-2 border-emerald-500/60 rounded-xl p-4 space-y-3 shadow-[0_0_30px_rgba(16,185,129,0.2)] relative">
          <div class="flex items-center justify-between">
            <span class="text-[10px] font-mono font-bold text-emerald-300 bg-emerald-950/90 px-2 py-0.5 rounded border border-emerald-700/80 shadow">
              👑 Majestic Monolith
            </span>
            <span class="text-2xl">🌐</span>
          </div>

          <!-- Live Browser Window Frame -->
          <div class="border border-emerald-500/40 rounded-lg p-2.5 bg-slate-900 shadow-inner space-y-2">
            <!-- Browser Header Bar -->
            <div class="flex items-center gap-1.5 pb-1.5 border-b border-slate-800 text-[9px] font-mono text-slate-400">
              <div class="flex gap-1">
                <span class="w-1.5 h-1.5 rounded-full bg-red-500"></span>
                <span class="w-1.5 h-1.5 rounded-full bg-amber-500"></span>
                <span class="w-1.5 h-1.5 rounded-full bg-emerald-500"></span>
              </div>
              <span class="bg-slate-950 px-2.5 py-0.5 rounded text-emerald-400 font-bold truncate w-full text-center border border-emerald-500/20">
                https://your-app.com
              </span>
            </div>
            
            <div class="flex items-center justify-between text-[10px] font-mono">
              <span class="text-emerald-400 font-bold flex items-center gap-1">
                <span class="w-2 h-2 rounded-full bg-emerald-400 animate-pulse"></span>
                Status 200 OK
              </span>
              <span class="text-emerald-300 font-semibold">Live Web Product</span>
            </div>
          </div>

          <div class="text-xs text-slate-200 font-semibold">
            Fully functional web app serving real users
          </div>
        </div>

      </div>
    </div>

    <!-- Bottom Takeaway Banner -->
    <div class="p-3 bg-slate-950 border border-slate-800 rounded-xl text-xs flex items-center justify-between">
      <span class="text-slate-300">
        🚀 <strong>Velocity Advantage:</strong> Rails turns raw ideas into shipping web products in record time.
      </span>
      <span class="text-[10px] font-mono text-red-400 bg-red-950/80 px-2.5 py-1 rounded border border-red-800 font-bold shrink-0 ml-2">
        10x Developer Velocity 💎
      </span>
    </div>

  </div>
</template>

<script setup>
</script>
