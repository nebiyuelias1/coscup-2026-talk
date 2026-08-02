<template>
  <div class="mobile-requirement-slide w-full my-auto flex flex-col justify-center">
    <!-- Header -->
    <div class="flex justify-between items-center mb-2">
      <span class="rails-badge">📱 Product Reality</span>
      <span class="text-xs font-mono text-slate-400">User Expectation & Growth</span>
    </div>

    <h2 class="text-2xl font-black tracking-tight text-white mb-3 text-left">
      Why Mobile Apps Are <span class="text-transparent bg-clip-text bg-gradient-to-r from-red-400 via-amber-300 to-red-500">Required</span> for Your Product
    </h2>

    <!-- Visual Journey Flow Diagram -->
    <div class="grid grid-cols-1 md:grid-cols-3 gap-3 mb-4">
      <!-- Stage 1 -->
      <div class="bg-slate-900/90 border border-red-500/30 rounded-xl p-3.5 relative overflow-hidden text-left shadow-lg">
        <div class="flex items-center justify-between mb-2">
          <span class="text-xs font-mono font-bold text-red-400 bg-red-950/80 px-2 py-0.5 rounded border border-red-800">Stage 1</span>
          <span class="text-lg">💎</span>
        </div>
        <h4 class="text-sm font-bold text-white mb-1">Start with Rails</h4>
        <p class="text-[11px] text-slate-300 leading-snug">
          Perfect for <strong>solo developers & small teams</strong>. Takes you from <strong>idea to reality faster</strong> than any stack.
        </p>
        <div class="mt-2.5 pt-2 border-t border-slate-800 text-[10px] font-mono text-red-300 flex items-center gap-1">
          ⚡ Solo Dev ➔ Instant MVP
        </div>
      </div>

      <!-- Stage 2 -->
      <div class="bg-slate-900/90 border border-amber-500/30 rounded-xl p-3.5 relative overflow-hidden text-left shadow-lg">
        <div class="flex items-center justify-between mb-2">
          <span class="text-xs font-mono font-bold text-amber-400 bg-amber-950/80 px-2 py-0.5 rounded border border-amber-800">Stage 2</span>
          <span class="text-lg">📢</span>
        </div>
        <h4 class="text-sm font-bold text-white mb-1">User Demand Hits</h4>
        <p class="text-[11px] text-slate-300 leading-snug">
          Users expect a <strong>Home Screen icon</strong> & push notifications, putting pressure on small teams to deliver.
        </p>
        <div class="mt-2.5 pt-2 border-t border-slate-800 text-[10px] font-mono text-amber-300 flex items-center gap-1">
          📲 Mobile Web is Not Enough
        </div>
      </div>

      <!-- Stage 3 -->
      <div class="bg-slate-900/90 border border-emerald-500/30 rounded-xl p-3.5 relative overflow-hidden text-left shadow-lg">
        <div class="flex items-center justify-between mb-2">
          <span class="text-xs font-mono font-bold text-emerald-400 bg-emerald-950/80 px-2 py-0.5 rounded border border-emerald-800">Stage 3</span>
          <span class="text-lg">📲</span>
        </div>
        <h4 class="text-sm font-bold text-white mb-1">Mandatory Mobile App</h4>
        <p class="text-[11px] text-slate-300 leading-snug">
          App Store presence unlocks maximum user reach, trust, retention & conversion.
        </p>
        <div class="mt-2.5 pt-2 border-t border-slate-800 text-[10px] font-mono text-emerald-300 flex items-center gap-1">
          🏆 Maximum Reach & Retention
        </div>
      </div>
    </div>

    <!-- Key Visual Stats Grid -->
    <div class="grid grid-cols-2 md:grid-cols-4 gap-3">
      <!-- Stat 1 -->
      <div class="p-3 bg-slate-950/80 rounded-xl border border-red-500/20 text-center shadow-md">
        <div class="text-2xl font-black text-red-400 font-mono tracking-tight">88%</div>
        <div class="text-[10px] text-slate-300 font-semibold uppercase mt-0.5">Mobile Time in Apps</div>
        <div class="text-[9px] text-slate-400 mt-1">vs. 12% on Mobile Browser</div>
      </div>

      <!-- Stat 2 -->
      <div class="p-3 bg-slate-950/80 rounded-xl border border-amber-500/20 text-center shadow-md">
        <div class="text-2xl font-black text-amber-400 font-mono tracking-tight">3.5x</div>
        <div class="text-[10px] text-slate-300 font-semibold uppercase mt-0.5">Higher Retention</div>
        <div class="text-[9px] text-slate-400 mt-1">App users return far more often</div>
      </div>

      <!-- Stat 3 -->
      <div class="p-3 bg-slate-950/80 rounded-xl border border-purple-500/20 text-center shadow-md">
        <div class="text-2xl font-black text-purple-400 font-mono tracking-tight">70%+</div>
        <div class="text-[10px] text-slate-300 font-semibold uppercase mt-0.5">Expect Push & Icon</div>
        <div class="text-[9px] text-slate-400 mt-1">Home screen presence = Trust</div>
      </div>

      <!-- Stat 4 -->
      <div class="p-3 bg-slate-950/80 rounded-xl border border-emerald-500/20 text-center shadow-md">
        <div class="text-2xl font-black text-emerald-400 font-mono tracking-tight">3x</div>
        <div class="text-[10px] text-slate-300 font-semibold uppercase mt-0.5">Higher Conversion</div>
        <div class="text-[9px] text-slate-400 mt-1">In-app purchase & checkout rate</div>
      </div>
    </div>

    <!-- Bottom Highlight Banner -->
    <div class="mt-3.5 p-2.5 bg-gradient-to-r from-red-950/70 via-slate-900 to-amber-950/70 border border-slate-800 rounded-xl flex items-center justify-between text-left px-4">
      <div class="flex items-center gap-2">
        <span class="text-base">💡</span>
        <span class="text-xs text-slate-200 font-medium">
          <strong>The Solo Dev Paradox:</strong> You launch fast on Rails, but user demand for mobile apps threatens to overwhelm small teams.
        </span>
      </div>
      <span class="text-[10px] font-mono text-amber-300 bg-slate-950 px-2 py-1 rounded border border-amber-500/30 shrink-0">
        Enter Hotwire Native 🚀
      </span>
    </div>
  </div>
</template>

<script setup>
</script>
