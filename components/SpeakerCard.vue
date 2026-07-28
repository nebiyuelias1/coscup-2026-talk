<template>
  <div
    class="speaker-card bg-slate-900/90 border border-red-500/30 rounded-2xl p-5 shadow-2xl backdrop-blur-md relative overflow-hidden my-2"
  >
    <!-- Background Glows -->
    <div
      class="absolute -right-16 -top-16 w-56 h-56 bg-red-600/15 rounded-full blur-3xl pointer-events-none"
    ></div>
    <div
      class="absolute -left-16 -bottom-16 w-56 h-56 bg-amber-600/10 rounded-full blur-3xl pointer-events-none"
    ></div>

    <div
      class="flex flex-col md:flex-row items-center md:items-start gap-5 relative z-10"
    >
      <!-- Avatar Container -->
      <div class="relative group shrink-0">
        <div
          class="w-36 h-36 rounded-2xl bg-gradient-to-tr from-red-600 via-amber-500 to-red-500 p-0.5 shadow-xl shadow-red-950/50"
        >
          <div
            class="w-full h-full rounded-[14px] bg-slate-950 flex items-center justify-center overflow-hidden"
          >
            <img
              src="/nebiyu.png"
              alt="Neba Headshot"
              class="w-full h-full object-cover object-top transition-transform duration-300 group-hover:scale-105"
            />
          </div>
        </div>
      </div>

      <!-- Info Column -->
      <div class="flex-1 text-left w-full space-y-3">
        <!-- Name & Badge Header -->
        <div
          class="flex flex-wrap items-center justify-between gap-2 border-b border-slate-800/80 pb-2"
        >
          <div>
            <h3
              class="text-xl font-black text-white tracking-tight m-0 flex items-center gap-2"
            >
              哈羅👋, 我是Neba
            </h3>
          </div>
        </div>

        <!-- 4 Highlight Cards Grid (2x2 layout on medium screens) -->
        <div class="grid grid-cols-1 md:grid-cols-2 gap-2.5">
          <!-- Card 1: 7+ Years Exp -->
          <div
            class="p-2.5 bg-slate-950/70 rounded-xl border border-red-500/20 hover:border-red-500/40 transition-colors shadow-sm"
          >
            <div
              class="text-red-400 font-bold text-xs mb-0.5 flex items-center gap-1.5"
            >
              <span>🚀</span> 7+ Years Experience
            </div>
            <p class="text-slate-300 m-0 text-[11px] leading-tight">
              Full-stack engineer building scalable web & mobile applications.
            </p>
          </div>

          <!-- Card 2: Ethiopia & Taiwan -->
          <div
            class="p-2.5 bg-slate-950/70 rounded-xl border border-blue-500/20 hover:border-blue-500/40 transition-colors shadow-sm"
          >
            <div
              class="text-blue-400 font-bold text-xs mb-0.5 flex items-center gap-1.5"
            >
              <span>🌍</span> Ethiopia 🇪🇹 ➔ Taiwan 🇹🇼
            </div>
            <p class="text-slate-300 m-0 text-[11px] leading-tight">
              Originally from Ethiopia, studying & working in Taiwan for 3
              years.
            </p>
          </div>

          <!-- Card 3: ASUS & 508.dev -->
          <div
            class="p-2.5 bg-slate-950/70 rounded-xl border border-emerald-500/20 hover:border-emerald-500/40 transition-colors shadow-sm"
          >
            <div
              class="text-emerald-400 font-bold text-xs mb-0.5 flex items-center gap-1.5"
            >
              <span>🏢</span> ASUS & 508.dev Co-op
            </div>
            <p class="text-slate-300 m-0 text-[11px] leading-tight">
              Currently working at ASUS and member of software engineer co-op
              508.dev.
            </p>
          </div>

          <!-- Card 4: Shipped Hotwire Native Apps -->
          <div
            class="p-2.5 bg-slate-950/70 rounded-xl border border-purple-500/20 hover:border-purple-500/40 transition-colors shadow-sm"
          >
            <div
              class="text-purple-400 font-bold text-xs mb-0.5 flex items-center gap-1.5"
            >
              <span>📱</span> Shipped on iOS & Android
            </div>
            <p class="text-slate-300 m-0 text-[11px] leading-tight">
              Shipped an app on iOS and Android using Hotwire Native.
            </p>
          </div>
        </div>

        <!-- Links Row -->
        <div
          class="flex flex-wrap items-center gap-4 pt-2 border-t border-slate-800/80 text-[11px]"
        >
          <a
            href="mailto:nebiyu@508.dev"
            class="flex items-center gap-1.5 text-red-400 hover:text-red-300 font-mono font-bold transition-colors"
          >
            ✉️ nebiyu@508.dev
          </a>
          <a
            href="https://github.com/nebiyuelias1"
            target="_blank"
            class="flex items-center gap-1.5 text-slate-300 hover:text-red-400 font-mono transition-colors"
          >
            <svg class="w-3.5 h-3.5 fill-current" viewBox="0 0 24 24">
              <path
                d="M12 0C5.37 0 0 5.37 0 12c0 5.31 3.435 9.795 8.205 11.385.6.105.825-.255.825-.57 0-.285-.015-1.23-.015-2.235-3.015.555-3.795-.735-4.035-1.41-.135-.345-.72-1.41-1.23-1.695-.42-.225-1.02-.78-.015-.795.945-.015 1.62.87 1.845 1.23 1.08 1.815 2.805 1.305 3.495.99.105-.78.42-1.305.765-1.605-2.67-.3-5.46-1.335-5.46-5.925 0-1.305.465-2.385 1.23-3.225-.12-.3-.54-1.53.12-3.18 0 0 1.005-.315 3.3 1.23.96-.27 1.98-.405 3-.405s2.04.135 3 .405c2.295-1.56 3.3-1.23 3.3-1.23.66 1.65.24 2.88.12 3.18.765.84 1.23 1.905 1.23 3.225 0 4.605-2.805 5.625-5.475 5.925.435.375.81 1.095.81 2.22 0 1.605-.015 2.895-.015 3.3 0 .315.225.69.825.57A12.02 12.02 0 0024 12c0-6.63-5.37-12-12-12z"
              />
            </svg>
            github.com/nebiyuelias1
          </a>
          <a
            href="https://github.com/nebiyuelias1/turbo-rails-react-native-starter"
            target="_blank"
            class="flex items-center gap-1 text-amber-400 hover:text-amber-300 font-mono font-bold transition-colors"
          >
            ⭐ Starter Template
          </a>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup></script>
