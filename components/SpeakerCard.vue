<template>
  <div class="speaker-card bg-slate-900/90 border border-red-500/30 rounded-xl p-4 shadow-2xl backdrop-blur-md relative overflow-hidden my-1">
    <!-- Ruby Background Glow -->
    <div class="absolute -right-16 -top-16 w-48 h-48 bg-red-600/20 rounded-full blur-3xl pointer-events-none"></div>
    <div class="absolute -left-16 -bottom-16 w-48 h-48 bg-blue-600/15 rounded-full blur-3xl pointer-events-none"></div>

    <div class="flex flex-col md:flex-row items-center md:items-start gap-4 relative z-10">
      <!-- Avatar Container -->
      <div class="relative group shrink-0">
        <div class="w-20 h-20 rounded-xl bg-gradient-to-tr from-red-600 to-amber-500 p-0.5 shadow-lg shadow-red-900/40">
          <div class="w-full h-full rounded-[10px] bg-slate-950 flex items-center justify-center overflow-hidden">
            <img src="/nebiyu.png" alt="Nebiyu Elias Talefe" class="w-full h-full object-cover object-top" />
          </div>
        </div>
        <div class="absolute -bottom-1.5 -right-1.5 bg-red-600 text-white text-[9px] font-bold px-1.5 py-0.5 rounded-full uppercase tracking-wider border border-slate-900 shadow">
          Rails Dev
        </div>
      </div>

      <!-- Info Column -->
      <div class="flex-1 text-left">
        <div class="flex flex-wrap items-center justify-between gap-1.5">
          <div>
            <h2 class="text-xl font-black tracking-tight text-white m-0">
              Nebiyu Elias Talefe
            </h2>
            <p class="text-red-400 font-semibold text-xs m-0 mt-0.5 flex items-center gap-1.5">
              <span>Full-Stack Engineer</span>
              <span class="w-1.5 h-1.5 rounded-full bg-red-500"></span>
              <span>7+ Years Experience</span>
            </p>
          </div>
          <span class="inline-flex items-center px-2.5 py-0.5 rounded-full text-[10px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/40 shadow-sm animate-pulse">
            ● Open for Opportunities
          </span>
        </div>

        <p class="text-slate-300 text-[11px] mt-1.5 leading-snug">
          Specializing in <strong>Ruby on Rails</strong>, <strong>Hotwire Native</strong>, <strong>Node.js</strong>, and <strong>PostgreSQL</strong>.
          Building scalable backends and high-performance hybrid mobile apps.
        </p>

        <!-- Skill Pills -->
        <div class="flex flex-wrap gap-1 mt-1.5">
          <span class="px-2 py-0.5 rounded text-[10px] font-semibold bg-red-950/60 text-red-300 border border-red-800/40">Ruby on Rails</span>
          <span class="px-2 py-0.5 rounded text-[10px] font-semibold bg-blue-950/60 text-blue-300 border border-blue-800/40">Hotwire Native</span>
          <span class="px-2 py-0.5 rounded text-[10px] font-semibold bg-purple-950/60 text-purple-300 border border-purple-800/40">Strada & Turbo</span>
          <span class="px-2 py-0.5 rounded text-[10px] font-semibold bg-amber-950/60 text-amber-300 border border-amber-800/40">PostgreSQL</span>
          <span class="px-2 py-0.5 rounded text-[10px] font-semibold bg-emerald-950/60 text-emerald-300 border border-emerald-800/40">Node.js / Express</span>
        </div>

        <!-- Links Row -->
        <div class="flex flex-wrap items-center gap-3 mt-2 pt-2 border-t border-slate-800/80 text-[10px]">
          <a href="mailto:nebiyu@508.dev" class="flex items-center gap-1 text-red-400 hover:text-red-300 font-mono font-bold transition-colors">
            ✉️ nebiyu@508.dev
          </a>
          <a href="https://github.com/nebiyuelias1" target="_blank" class="flex items-center gap-1 text-slate-300 hover:text-red-400 font-mono transition-colors">
            <svg class="w-3.5 h-3.5 fill-current" viewBox="0 0 24 24"><path d="M12 0C5.37 0 0 5.37 0 12c0 5.31 3.435 9.795 8.205 11.385.6.105.825-.255.825-.57 0-.285-.015-1.23-.015-2.235-3.015.555-3.795-.735-4.035-1.41-.135-.345-.72-1.41-1.23-1.695-.42-.225-1.02-.78-.015-.795.945-.015 1.62.87 1.845 1.23 1.08 1.815 2.805 1.305 3.495.99.105-.78.42-1.305.765-1.605-2.67-.3-5.46-1.335-5.46-5.925 0-1.305.465-2.385 1.23-3.225-.12-.3-.54-1.53.12-3.18 0 0 1.005-.315 3.3 1.23.96-.27 1.98-.405 3-.405s2.04.135 3 .405c2.295-1.56 3.3-1.23 3.3-1.23.66 1.65.24 2.88.12 3.18.765.84 1.23 1.905 1.23 3.225 0 4.605-2.805 5.625-5.475 5.925.435.375.81 1.095.81 2.22 0 1.605-.015 2.895-.015 3.3 0 .315.225.69.825.57A12.02 12.02 0 0024 12c0-6.63-5.37-12-12-12z"/></svg>
            github.com/nebiyuelias1
          </a>
          <a href="https://github.com/nebiyuelias1/turbo-rails-react-native-starter" target="_blank" class="flex items-center gap-1 text-amber-400 hover:text-amber-300 font-mono transition-colors">
            ⭐ Starter Template
          </a>
          <div class="flex items-center gap-1 ml-auto bg-slate-950 px-2 py-0.5 rounded border border-slate-800">
            <img src="/coscup_logo.png" alt="COSCUP Logo" class="h-3 object-contain" />
            <span class="text-slate-300 font-bold text-[10px]">2026 Speaker</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
</script>
