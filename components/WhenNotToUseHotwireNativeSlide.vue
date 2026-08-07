<template>
  <div class="when-not-to-use-hotwire-native-slide w-full my-auto flex flex-col justify-center text-left">
    
    <!-- Header Badge -->
    <div class="flex justify-between items-center mb-2">
      <span class="rails-badge font-bold">⚠️ Reality Check</span>
      <span class="text-xs font-mono text-slate-400">Choosing The Right Tool</span>
    </div>

    <!-- Main Title -->
    <h2 class="text-3xl font-black tracking-tight text-white mb-5">
      When <span class="text-red-500">NOT</span> To Use Hotwire Native 🚫
    </h2>

    <!-- 2 Balanced Cards -->
    <div class="grid grid-cols-1 md:grid-cols-2 gap-5 mb-4">
      
      <!-- Scenario 1: Heavy Games / AR -->
      <div class="bg-slate-900/90 border border-red-500/40 rounded-2xl p-5 shadow-2xl space-y-3 flex flex-col justify-between">
        <div>
          <div class="flex items-center gap-3 mb-2">
            <span class="text-3xl">🎮</span>
            <div>
              <h3 class="text-lg font-black text-white m-0">3D Games & AR Apps</h3>
              <p class="text-xs text-red-400 font-mono m-0 mt-0.5">Pokémon GO, Pikmin Bloom</p>
            </div>
          </div>
          <p class="text-xs text-slate-300 leading-relaxed m-0">
            For GPU-intensive 3D graphics, real-time physics, or heavy AR camera engines.
          </p>
        </div>

        <div class="pt-3 border-t border-slate-800 flex items-center justify-between text-xs font-mono">
          <span class="text-slate-400">Use Instead:</span>
          <span class="text-red-400 font-bold bg-red-950/80 px-3 py-1 rounded-lg border border-red-800">Unity / Metal Engine</span>
        </div>
      </div>

      <!-- Scenario 2: Massive Engineering Teams -->
      <div class="bg-slate-900/90 border border-amber-500/40 rounded-2xl p-5 shadow-2xl space-y-3 flex flex-col justify-between">
        <div>
          <div class="flex items-center gap-3 mb-2">
            <span class="text-3xl">🏢</span>
            <div>
              <h3 class="text-lg font-black text-white m-0">Massive Mobile Teams</h3>
              <p class="text-xs text-amber-400 font-mono m-0 mt-0.5">Dedicated Mobile Engineering Teams</p>
            </div>
          </div>
          <p class="text-xs text-slate-300 leading-relaxed m-0">
            When you have large budgets and dedicated, separate iOS & Android engineering orgs.
          </p>
        </div>

        <div class="pt-3 border-t border-slate-800 flex items-center justify-between text-xs font-mono">
          <span class="text-slate-400">Use Instead:</span>
          <span class="text-amber-400 font-bold bg-amber-950/80 px-3 py-1 rounded-lg border border-amber-800">Separate Native Stacks</span>
        </div>
      </div>

    </div>

    <!-- Bottom Takeaway Banner -->
    <div class="p-3 bg-slate-950 border border-slate-800 rounded-xl text-xs flex items-center justify-between">
      <span class="text-slate-300">
        💡 <strong>Sweet Spot:</strong> SaaS, Marketplaces, E-Commerce & Content Apps built by lean teams.
      </span>
      <span class="text-[10px] font-mono text-emerald-400 bg-emerald-950/80 px-2.5 py-1 rounded border border-emerald-800 font-bold shrink-0 ml-2">
        Maximum Leverage ⚡
      </span>
    </div>

  </div>
</template>

<script setup>
</script>
