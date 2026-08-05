<template>
  <div class="rails-contrarian-slide w-full my-auto flex flex-col justify-center">
    <!-- Header -->
    <div class="flex justify-between items-center mb-1">
      <span class="rails-badge font-bold">🥊 The Rails Philosophy</span>
      <span class="text-xs font-mono text-slate-400">Pragmatism Over Hype</span>
    </div>

    <h2 class="text-2xl font-black tracking-tight text-white mb-3 text-left flex items-center justify-between">
      <span>Embrace Being <span class="text-transparent bg-clip-text bg-gradient-to-r from-red-400 via-amber-300 to-red-500">Contrarian 🎯</span></span>
      <span class="text-xs font-mono text-amber-300 bg-amber-950/80 px-2.5 py-1 rounded border border-amber-500/40">
        Simplicity > Hype ⚡
      </span>
    </h2>

    <!-- 4 Contrarian Pillars Grid -->
    <div class="grid grid-cols-1 md:grid-cols-2 gap-3 mb-3 text-left">
      
      <!-- 1. Solid Cache / Queue -->
      <div class="bg-slate-900/90 border border-red-500/30 rounded-xl p-3.5 shadow-lg flex flex-col justify-between">
        <div>
          <div class="flex items-center justify-between mb-1.5">
            <span class="text-xs font-bold text-red-400 flex items-center gap-1">
              🗄️ Solid Cache & Queue
            </span>
            <span class="text-[9px] font-mono bg-red-950 text-red-300 px-1.5 py-0.5 rounded border border-red-800">
              Database as Infra
            </span>
          </div>
          <div class="text-[10px] text-slate-400 mb-1">
            <s>Industry: "Must run Redis & extra RAM clusters"</s>
          </div>
          <p class="text-xs text-slate-200 leading-snug m-0">
            <strong>Rails Way:</strong> Use your SQL database for cache & background jobs (SolidCache / SolidQueue). Zero extra server overhead.
          </p>
        </div>
      </div>

      <!-- 2. ActiveRecord Introspection -->
      <div class="bg-slate-900/90 border border-amber-500/30 rounded-xl p-3.5 shadow-lg flex flex-col justify-between">
        <div>
          <div class="flex items-center justify-between mb-1.5">
            <span class="text-xs font-bold text-amber-400 flex items-center gap-1">
              🔍 Schema Introspection
            </span>
            <span class="text-[9px] font-mono bg-amber-950 text-amber-300 px-1.5 py-0.5 rounded border border-amber-800">
              Zero Boilerplate
            </span>
          </div>
          <div class="text-[10px] text-slate-400 mb-1">
            <s>Industry: "Manually define & sync every DB field"</s>
          </div>
          <p class="text-xs text-slate-200 leading-snug m-0">
            <strong>Rails Way:</strong> ActiveRecord inspects database schema at runtime automatically. Zero schema drift & minimal boilerplate.
          </p>
        </div>
      </div>

      <!-- 3. Majestic Monolith -->
      <div class="bg-slate-900/90 border border-purple-500/30 rounded-xl p-3.5 shadow-lg flex flex-col justify-between">
        <div>
          <div class="flex items-center justify-between mb-1.5">
            <span class="text-xs font-bold text-purple-300 flex items-center gap-1">
              🏰 Majestic Monolith
            </span>
            <span class="text-[9px] font-mono bg-purple-950 text-purple-300 px-1.5 py-0.5 rounded border border-purple-800">
              Solo Dev Speed
            </span>
          </div>
          <div class="text-[10px] text-slate-400 mb-1">
            <s>Industry: "Split into 50 Kubernetes microservices"</s>
          </div>
          <p class="text-xs text-slate-200 leading-snug m-0">
            <strong>Rails Way:</strong> One cohesive codebase powers your product. 1 developer can build & deploy features at 10x speed.
          </p>
        </div>
      </div>

      <!-- 4. HTML Over The Wire (Hotwire Native) -->
      <div class="bg-slate-900/90 border border-emerald-500/30 rounded-xl p-3.5 shadow-lg flex flex-col justify-between">
        <div>
          <div class="flex items-center justify-between mb-1.5">
            <span class="text-xs font-bold text-emerald-400 flex items-center gap-1">
              ⚡ HTML Over The Wire
            </span>
            <span class="text-[9px] font-mono bg-emerald-950 text-emerald-300 px-1.5 py-0.5 rounded border border-emerald-800">
              Hotwire Native
            </span>
          </div>
          <div class="text-[10px] text-slate-400 mb-1">
            <s>Industry: "Build complex SPAs & mobile API stacks"</s>
          </div>
          <p class="text-xs text-slate-200 leading-snug m-0">
            <strong>Rails Way:</strong> Render HTML on server & stream directly inside native mobile shells. Web, iOS & Android from 1 app.
          </p>
        </div>
      </div>

    </div>

    <!-- Bottom Takeaway Banner -->
    <div class="p-2.5 bg-slate-950 border border-slate-800 rounded-xl text-left flex items-center justify-between text-xs">
      <span class="text-slate-300">
        💡 <strong>The Secret:</strong> Being contrarian isn't about being stubborn — it's about choosing <strong>shipping speed over complexity</strong>.
      </span>
      <span class="text-[10px] font-mono text-red-400 bg-red-950/80 px-2 py-0.5 rounded border border-red-700 shrink-0 font-bold ml-2">
        The Rails Advantage 💎
      </span>
    </div>

  </div>
</template>

<script setup>
</script>
