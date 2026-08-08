<template>
  <div class="idea-to-reality-slide w-full my-auto flex flex-col justify-center text-left">
    
    <!-- Header Badge -->
    <div class="flex justify-between items-center mb-2">
      <span class="rails-badge font-bold">{{ currentLang === 'zh' ? '💡 創立之初' : '💡 The Genesis' }}</span>
      <span class="text-xs font-mono text-slate-400">{{ currentLang === 'zh' ? '從 0 到 1 的轉變' : '0 to 1 Transformation' }}</span>
    </div>

    <!-- Main Title -->
    <h2 class="text-3xl font-black tracking-tight text-white mb-6">
      <template v-if="currentLang === 'zh'">
        將 <span class="text-amber-400">點子 (Idea)</span> 轉化為 <span class="text-emerald-400">產品 (Product) 🚀</span>
      </template>
      <template v-else>
        Turning an <span class="text-amber-400">Idea</span> into a <span class="text-emerald-400">Product 🚀</span>
      </template>
    </h2>

    <!-- Visual 3-Node Transformation Diagram -->
    <div class="relative bg-slate-900/90 border border-red-500/40 rounded-2xl p-8 shadow-2xl backdrop-blur-md mb-5 overflow-hidden">
      
      <!-- Background Ambient Glows -->
      <div class="absolute -top-12 -left-12 w-48 h-48 bg-amber-500/10 rounded-full blur-3xl pointer-events-none"></div>
      <div class="absolute -bottom-12 -right-12 w-48 h-48 bg-emerald-500/15 rounded-full blur-3xl pointer-events-none"></div>

      <div class="grid grid-cols-1 md:grid-cols-11 gap-3 items-center relative z-10">
        
        <!-- Left: Idea (Lightbulb) [Cols 1-4] -->
        <div class="md:col-span-4 bg-slate-950/90 border-2 border-amber-500/40 rounded-2xl p-6 shadow-xl text-center space-y-2">
          <div class="w-16 h-16 rounded-2xl bg-amber-500/20 border border-amber-500/40 text-amber-400 flex items-center justify-center text-4xl mx-auto shadow-lg">
            💡
          </div>
          <h3 class="text-xl font-black text-white m-0">{{ currentLang === 'zh' ? '點子 (Idea)' : 'Idea' }}</h3>
        </div>

        <!-- Center: Rails (Engine Bridge) [Cols 5-7] -->
        <div class="md:col-span-3 flex flex-col items-center justify-center text-center py-2 relative">
          <!-- Connecting Line & Larger Gem Badge -->
          <div class="hidden md:flex items-center w-full relative">
            <div class="h-0.5 bg-gradient-to-r from-amber-500 via-red-500 to-emerald-500 w-full"></div>
            <div class="absolute inset-0 flex items-center justify-center">
              <div class="bg-red-950 border-2 border-red-500 text-white px-4 py-2.5 rounded-full font-mono text-base font-black shadow-2xl flex items-center gap-2">
                <img src="/ruby_taiwan_logo.svg" alt="Rails Logo" class="h-8 w-8 object-contain" />
                <span class="text-red-200">Rails</span>
              </div>
            </div>
          </div>
        </div>

        <!-- Right: Product (Live Web App) [Cols 8-11] -->
        <div class="md:col-span-4 bg-slate-950/95 border-2 border-emerald-500/60 rounded-2xl p-6 shadow-[0_0_30px_rgba(16,185,129,0.2)] text-center space-y-2">
          <div class="w-16 h-16 rounded-2xl bg-emerald-500/20 border border-emerald-500/40 text-emerald-400 flex items-center justify-center text-4xl mx-auto shadow-lg">
            🌐
          </div>
          <h3 class="text-xl font-black text-white m-0">{{ currentLang === 'zh' ? '產品 (Product)' : 'Product' }}</h3>
        </div>

      </div>
    </div>

    <!-- Bottom Takeaway Banner -->
    <div class="p-3 bg-slate-950 border border-slate-800 rounded-xl text-xs flex items-center justify-between">
      <span class="text-slate-300">
        🚀 <strong>The Rails Advantage:</strong> {{ currentLang === 'zh' ? '比任何其他框架更快速地將靈感轉化為實際上線的產品。' : 'Turns raw ideas into shipping products faster than any other framework.' }}
      </span>
      <span class="text-[10px] font-mono text-red-400 bg-red-950/80 px-2.5 py-1 rounded border border-red-800 font-bold shrink-0 ml-2">
        0 to 1 Velocity 💎
      </span>
    </div>

  </div>
</template>

<script setup>
import { currentLang } from '../composables/useLang'
</script>
