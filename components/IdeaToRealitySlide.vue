<template>
  <div class="idea-to-reality-slide w-full my-auto flex flex-col justify-center text-left">
    
    <!-- Header Badge -->
    <div class="flex justify-between items-center mb-2">
      <span class="rails-badge font-bold">💡 The Genesis</span>
      <span class="text-xs font-mono text-slate-400">0 to 1 Speed</span>
    </div>

    <!-- Main Title -->
    <h2 class="text-3xl font-black tracking-tight text-white mb-6">
      Every Great Product Starts With an <span class="text-red-500">Idea 🚀</span>
    </h2>

    <!-- Visual Transformation Flow -->
    <div class="bg-slate-900/90 border border-red-500/40 rounded-2xl p-6 shadow-2xl backdrop-blur-md mb-5">
      <div class="grid grid-cols-1 md:grid-cols-3 gap-4 items-center text-center">
        
        <!-- Step 1: Raw Idea -->
        <div class="p-5 bg-slate-950/80 rounded-xl border border-slate-800 space-y-2 flex flex-col items-center justify-center">
          <div class="w-14 h-14 rounded-2xl bg-amber-500/20 border border-amber-500/40 text-amber-400 flex items-center justify-center text-3xl shadow-lg">
            💡
          </div>
          <h3 class="text-base font-bold text-white m-0">1. The Idea</h3>
          <p class="text-xs text-slate-400 m-0">A vision to solve a real user problem</p>
        </div>

        <!-- Step 2: Rails Acceleration -->
        <div class="p-5 bg-red-950/40 rounded-xl border border-red-500/40 space-y-2 flex flex-col items-center justify-center relative">
          <div class="w-14 h-14 rounded-2xl bg-red-600/20 border border-red-500/60 flex items-center justify-center shadow-lg p-2">
            <img src="/ruby_taiwan_logo.svg" alt="Ruby on Rails Logo" class="h-10 w-10 object-contain" />
          </div>
          <h3 class="text-base font-bold text-red-300 m-0">2. Rails Speed 💎</h3>
          <p class="text-xs text-slate-300 m-0">Unmatched full-stack shipping velocity</p>
        </div>

        <!-- Step 3: Production Web App -->
        <div class="p-5 bg-slate-950/80 rounded-xl border border-slate-800 space-y-2 flex flex-col items-center justify-center">
          <div class="w-14 h-14 rounded-2xl bg-emerald-500/20 border border-emerald-500/40 text-emerald-400 flex items-center justify-center text-3xl shadow-lg">
            🌐
          </div>
          <h3 class="text-base font-bold text-white m-0">3. Live Web App</h3>
          <p class="text-xs text-slate-400 m-0">Production product shipped in record time</p>
        </div>

      </div>
    </div>

    <!-- Bottom Takeaway Banner -->
    <div class="p-3 bg-slate-950 border border-slate-800 rounded-xl text-xs flex items-center justify-between">
      <span class="text-slate-300">
        ⚡ <strong>The Rails Advantage:</strong> Rails turns raw ideas into shipping web products faster than any other stack.
      </span>
      <span class="text-[10px] font-mono text-red-400 bg-red-950/80 px-2.5 py-1 rounded border border-red-800 font-bold shrink-0 ml-2">
        0 to 1 Velocity 🚀
      </span>
    </div>

  </div>
</template>

<script setup>
</script>
