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
          <div class="flex items-center gap-3 flex-wrap">
            <h3
              class="text-xl font-black text-white tracking-tight m-0 flex items-center gap-2"
            >
              {{ currentLang === 'zh' ? '哈囉👋, 我是 Neba' : 'Hello 👋, I am Neba' }}
            </h3>
          </div>
        </div>

        <!-- Highlight Bullet List -->
        <ul class="space-y-3 my-2 p-0 list-none text-left">
          <!-- Bullet 1: 7+ Years Exp -->
          <li
            class="flex items-start gap-2.5 text-xs text-slate-300 leading-relaxed"
          >
            <span class="text-red-400 text-sm leading-none mt-0.5 shrink-0"
              >🚀</span
            >
            <div>
              <span class="text-red-400 font-bold mr-1.5"
                >{{ currentLang === 'zh' ? '7+ 年全棧開發經驗' : '7+ Years Experience' }}</span
              >
            </div>
          </li>

          <!-- Bullet 2: Ethiopia & Taiwan -->
          <li
            class="flex items-start gap-2.5 text-xs text-slate-300 leading-relaxed"
          >
            <span class="text-blue-400 text-sm leading-none mt-0.5 shrink-0"
              >🌍</span
            >
            <div>
              <span class="text-blue-400 font-bold mr-1.5"
                >{{ currentLang === 'zh' ? '埃塞俄比亞 🇪🇹 ➔ 台灣 🇹🇼 (在台學習與工作 3 年)' : 'Ethiopia 🇪🇹 ➔ Taiwan 🇹🇼 (3 years in TW)' }}</span
              >
            </div>
          </li>

          <!-- Bullet 3: ASUS & 508.dev -->
          <li
            class="flex items-start gap-2.5 text-xs text-slate-300 leading-relaxed"
          >
            <span class="text-emerald-400 text-sm leading-none mt-0.5 shrink-0"
              >🏢</span
            >
            <div>
              <span class="text-emerald-400 font-bold mr-1.5"
                >{{ currentLang === 'zh' ? '任職於 ASUS & 508.dev 工程合作社成員' : 'ASUS & 508.dev Co-op Member' }}</span
              >
            </div>
          </li>

          <!-- Bullet 4: Shipped & Currently Building Hotwire Native Apps -->
          <li
            class="flex items-start gap-2.5 text-xs text-slate-300 leading-relaxed"
          >
            <span class="text-purple-400 text-sm leading-none mt-0.5 shrink-0"
              >📱</span
            >
            <div>
              <span class="text-purple-400 font-bold mr-1.5"
                >{{ currentLang === 'zh' ? '已上架並持續使用 Hotwire Native 開發 Mobile App' : 'Shipped & Building with Hotwire Native' }}</span
              >
            </div>
          </li>

          <!-- Bullet 5: Rubyist -->
          <li
            class="flex items-start gap-2.5 text-xs text-slate-300 leading-relaxed"
          >
            <span class="text-rose-400 text-sm leading-none mt-0.5 shrink-0"
              >💎</span
            >
            <div>
              <span class="text-rose-400 font-bold mr-1.5">{{ currentLang === 'zh' ? 'Rubyist 熱情狂熱者' : 'Rubyist' }}</span>
            </div>
          </li>

          <!-- Bullet 6: Omarchy OS -->
          <li
            class="flex items-center gap-2.5 text-xs text-slate-300 leading-relaxed"
          >
            <span class="text-cyan-400 text-sm leading-none shrink-0">🐧</span>
            <div class="flex items-center gap-2 flex-wrap">
              <span class="text-cyan-400 font-bold">{{ currentLang === 'zh' ? '作業系統與環境:' : 'OS & Environment:' }}</span>
              <span class="text-slate-200 font-mono font-bold text-[11px]"
                >I use omarchy btw</span
              >
            </div>
          </li>
        </ul>

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

<script setup>
import { currentLang } from '../composables/useLang'
</script>
