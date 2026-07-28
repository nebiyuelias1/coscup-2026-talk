<template>
  <footer 
    v-if="$slidev.nav.currentPage > 1" 
    class="absolute bottom-2 left-6 right-6 flex items-center justify-between text-[11px] font-mono text-slate-400 border-t border-slate-800/70 pt-1.5 z-50 pointer-events-none"
  >
    <!-- Left: COSCUP Logo & Year -->
    <div class="flex items-center gap-2 pointer-events-auto">
      <img src="/coscup_logo.png" alt="COSCUP Logo" class="h-3.5 w-auto object-contain opacity-90" />
      <span class="text-[10px] font-bold text-slate-300">2026</span>
    </div>

    <!-- Center: Slide / Page Number (True Absolute Centering) -->
    <div class="absolute left-1/2 -translate-x-1/2 flex items-center gap-1 font-mono text-[10px] text-slate-300 bg-slate-900/90 px-2.5 py-0.5 rounded-full border border-slate-800/90 shadow-sm pointer-events-auto">
      <span class="text-red-400 font-bold">{{ $slidev.nav.currentPage }}</span>
      <span class="text-slate-500">/</span>
      <span class="text-slate-400">{{ $slidev.nav.total }}</span>
    </div>

    <!-- Right: Email & Portfolio Link -->
    <div class="flex items-center gap-2.5 pointer-events-auto text-[10px]">
      <a href="mailto:nebiyu@508.dev" class="text-red-300 font-bold hover:text-red-200 transition-colors">
        ✉️ nebiyu@508.dev
      </a>
      <span class="text-slate-600">•</span>
      <a href="https://netale.et/#talks" target="_blank" class="text-emerald-400 hover:text-emerald-300 font-bold transition-colors underline">
        netale.et/#talks
      </a>
    </div>
  </footer>
</template>

<script setup>
</script>
