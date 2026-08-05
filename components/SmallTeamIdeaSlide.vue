<template>
  <div class="small-team-idea-slide w-full my-auto flex flex-col justify-center">
    <!-- Header -->
    <div class="flex justify-between items-center mb-2">
      <span class="rails-badge font-bold">💡 The Lightbulb Moment</span>
      <span class="text-xs font-mono text-slate-400">Small Team Strategy</span>
    </div>

    <h2 class="text-3xl font-black tracking-tight text-white mb-3 text-left">
      But Wait... We're a <span class="text-transparent bg-clip-text bg-gradient-to-r from-amber-300 via-yellow-400 to-red-400">Small Team! 🚀</span>
    </h2>

    <p class="text-sm text-slate-300 text-left mb-5">
      What if we can use the <strong>Rails app we already have</strong> to also build our mobile app?
    </p>

    <!-- 3 Simple Punchy Strategy Cards -->
    <div class="grid grid-cols-1 md:grid-cols-3 gap-4 mb-4 text-left">
      
      <!-- Card 1 -->
      <div class="bg-slate-900/90 border border-amber-500/30 rounded-2xl p-4 shadow-xl flex flex-col justify-between">
        <div>
          <div class="w-10 h-10 rounded-xl bg-amber-500/20 text-amber-400 font-bold flex items-center justify-center text-xl mb-3 border border-amber-500/30">
            💎
          </div>
          <h3 class="text-base font-bold text-white mb-1.5">100% Code Reuse</h3>
          <p class="text-xs text-slate-300 leading-relaxed m-0">
            We already built controllers, models, and ERB views. Why rewrite them from scratch?
          </p>
        </div>
        <div class="mt-4 pt-2 border-t border-slate-800 text-[10px] font-mono text-amber-300">
          Zero logic duplication 🎯
        </div>
      </div>

      <!-- Card 2 -->
      <div class="bg-slate-900/90 border border-blue-500/30 rounded-2xl p-4 shadow-xl flex flex-col justify-between">
        <div>
          <div class="w-10 h-10 rounded-xl bg-blue-500/20 text-blue-400 font-bold flex items-center justify-center text-xl mb-3 border border-blue-500/30">
            🌐
          </div>
          <h3 class="text-base font-bold text-white mb-1.5">WebViews as Mobile Shell</h3>
          <p class="text-xs text-slate-300 leading-relaxed m-0">
            Render our existing Rails web pages directly inside iOS & Android WebView frames!
          </p>
        </div>
        <div class="mt-4 pt-2 border-t border-slate-800 text-[10px] font-mono text-blue-300">
          Instant cross-platform ⚡
        </div>
      </div>

      <!-- Card 3 -->
      <div class="bg-slate-900/90 border border-emerald-500/30 rounded-2xl p-4 shadow-xl flex flex-col justify-between">
        <div>
          <div class="w-10 h-10 rounded-xl bg-emerald-500/20 text-emerald-400 font-bold flex items-center justify-center text-xl mb-3 border border-emerald-500/30">
            🚀
          </div>
          <h3 class="text-base font-bold text-white mb-1.5">Deploy Without Waiting</h3>
          <p class="text-xs text-slate-300 leading-relaxed m-0">
            Fix a bug or ship copy updates on the server — live instantly on Web, iOS & Android.
          </p>
        </div>
        <div class="mt-4 pt-2 border-t border-slate-800 text-[10px] font-mono text-emerald-300">
          No App Store queue delays 🕒
        </div>
      </div>

    </div>

    <!-- Bottom Question Callout Banner -->
    <div class="p-3 bg-slate-950 border border-slate-800 rounded-xl text-left flex items-center justify-between">
      <span class="text-xs text-slate-200 font-medium">
        🤔 <em>"Why don't we just load our web app inside WebViews and ship it today?"</em>
      </span>
      <span class="text-[10px] font-mono text-amber-300 bg-amber-950/80 px-2.5 py-1 rounded border border-amber-500/40 shrink-0 font-bold">
        Pragmatic Solo Dev Choice 💡
      </span>
    </div>

  </div>
</template>

<script setup>
</script>
