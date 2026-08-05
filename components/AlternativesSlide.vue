<template>
  <div class="alternatives-slide w-full my-auto flex flex-col justify-center">
    
    <!-- Progression Complexity Meter Bar (Shown on all single-approach slides) -->
    <div v-if="approach && approach !== 'all'" class="mb-4 text-left">
      <div class="flex items-center justify-between mb-1.5">
        <span class="rails-badge">⚖️ Alternative {{ currentStep }} of 3</span>
        <div class="flex items-center gap-2">
          <span class="text-xs font-mono text-slate-400">Overhead & Complexity:</span>
          <span :class="['text-xs font-mono font-bold px-2 py-0.5 rounded border', complexityBadgeStyle]">
            {{ complexityLabel }}
          </span>
        </div>
      </div>

      <!-- 3-Segment Visual Complexity Bar -->
      <div class="grid grid-cols-3 gap-2">
        <div 
          :class="[
            'h-1.5 rounded-full transition-all',
            currentStep >= 1 ? 'bg-amber-400 shadow-sm shadow-amber-500/50' : 'bg-slate-800'
          ]"></div>
        <div 
          :class="[
            'h-1.5 rounded-full transition-all',
            currentStep >= 2 ? 'bg-orange-500 shadow-sm shadow-orange-500/50' : 'bg-slate-800'
          ]"></div>
        <div 
          :class="[
            'h-1.5 rounded-full transition-all',
            currentStep >= 3 ? 'bg-red-500 shadow-sm shadow-red-500/50' : 'bg-slate-800'
          ]"></div>
      </div>
    </div>

    <!-- 1. PWA (Level 1 / 3) -->
    <template v-if="approach === 'pwa'">
      <h2 class="text-2xl font-black tracking-tight text-white mb-4 text-left flex items-center justify-between">
        <span>1. Progressive Web Apps <span class="text-amber-400">(PWAs) 🌐</span></span>
        <span class="text-xs font-mono text-amber-300 bg-amber-950/80 px-3 py-1 rounded-full border border-amber-800">
          ⚠️ Low Setup / High Friction
        </span>
      </h2>

      <!-- 3 Clean Punchy Cards -->
      <div class="grid grid-cols-1 md:grid-cols-3 gap-4 mb-4 text-left">
        <div class="bg-slate-900/90 border border-amber-500/30 rounded-2xl p-4 shadow-xl flex flex-col justify-between">
          <div>
            <div class="text-2xl mb-2">📲</div>
            <h3 class="text-sm font-bold text-white mb-1">No App Store Presence</h3>
            <p class="text-xs text-slate-300 leading-relaxed m-0">
              Users search App Store & Play Store — not browser web links.
            </p>
          </div>
        </div>

        <div class="bg-slate-900/90 border border-amber-500/30 rounded-2xl p-4 shadow-xl flex flex-col justify-between">
          <div>
            <div class="text-2xl mb-2">🍎</div>
            <h3 class="text-sm font-bold text-white mb-1">iOS Safari Quirks</h3>
            <p class="text-xs text-slate-300 leading-relaxed m-0">
              Flaky push notifications & strict WebKit storage limits.
            </p>
          </div>
        </div>

        <div class="bg-slate-900/90 border border-amber-500/30 rounded-2xl p-4 shadow-xl flex flex-col justify-between">
          <div>
            <div class="text-2xl mb-2">⚡</div>
            <h3 class="text-sm font-bold text-white mb-1">Web-Only Feel</h3>
            <p class="text-xs text-slate-300 leading-relaxed m-0">
              Lacks native 60fps animations, native sheets & system tabs.
            </p>
          </div>
        </div>
      </div>

      <!-- Bottom Simple Callout -->
      <div class="p-3 bg-slate-950 border border-slate-800 rounded-xl text-left flex items-center justify-between">
        <span class="text-xs text-slate-300">💡 <strong>Verdict:</strong> Easiest to deploy, but weak user reach & retention.</span>
        <span class="text-[10px] font-mono text-amber-400">Level 1 Complexity</span>
      </div>
    </template>

    <!-- 2. REACT NATIVE / FLUTTER (Level 2 / 3) -->
    <template v-if="approach === 'react-native'">
      <h2 class="text-2xl font-black tracking-tight text-white mb-4 text-left flex items-center justify-between">
        <span>2. React Native / Flutter <span class="text-orange-400">⚛️</span></span>
        <span class="text-xs font-mono text-orange-300 bg-orange-950/80 px-3 py-1 rounded-full border border-orange-800">
          📦 Medium / API & State Tax
        </span>
      </h2>

      <!-- 3 Clean Punchy Cards -->
      <div class="grid grid-cols-1 md:grid-cols-3 gap-4 mb-4 text-left">
        <div class="bg-slate-900/90 border border-orange-500/30 rounded-2xl p-4 shadow-xl flex flex-col justify-between">
          <div>
            <div class="text-2xl mb-2">🔌</div>
            <h3 class="text-sm font-bold text-white mb-1">Heavy JSON API Tax</h3>
            <p class="text-xs text-slate-300 leading-relaxed m-0">
              Must write, version, and sync REST/GraphQL endpoints for every screen.
            </p>
          </div>
        </div>

        <div class="bg-slate-900/90 border border-orange-500/30 rounded-2xl p-4 shadow-xl flex flex-col justify-between">
          <div>
            <div class="text-2xl mb-2">🔄</div>
            <h3 class="text-sm font-bold text-white mb-1">Double State Management</h3>
            <p class="text-xs text-slate-300 leading-relaxed m-0">
              Database state on server vs client JS state (Redux/Zustand) on mobile.
            </p>
          </div>
        </div>

        <div class="bg-slate-900/90 border border-orange-500/30 rounded-2xl p-4 shadow-xl flex flex-col justify-between">
          <div>
            <div class="text-2xl mb-2">🗑️</div>
            <h3 class="text-sm font-bold text-white mb-1">Discards Server HTML</h3>
            <p class="text-xs text-slate-300 leading-relaxed m-0">
              Completely bypasses existing Rails views, ERB templates & helpers.
            </p>
          </div>
        </div>
      </div>

      <!-- Bottom Simple Callout -->
      <div class="p-3 bg-slate-950 border border-slate-800 rounded-xl text-left flex items-center justify-between">
        <span class="text-xs text-slate-300">💡 <strong>Verdict:</strong> Cross-platform UI, but doubles backend & state overhead.</span>
        <span class="text-[10px] font-mono text-orange-400">Level 2 Complexity</span>
      </div>
    </template>

    <!-- 3. FULL NATIVE (Level 3 / 3) -->
    <template v-if="approach === 'native'">
      <h2 class="text-2xl font-black tracking-tight text-white mb-4 text-left flex items-center justify-between">
        <span>3. Separate Native Apps <span class="text-red-400">(Swift & Kotlin) 📱</span></span>
        <span class="text-xs font-mono text-red-300 bg-red-950/80 px-3 py-1 rounded-full border border-red-800">
          🔴 Highest / Tripled Cost
        </span>
      </h2>

      <!-- 3 Clean Punchy Cards -->
      <div class="grid grid-cols-1 md:grid-cols-3 gap-4 mb-4 text-left">
        <div class="bg-slate-900/90 border border-red-500/30 rounded-2xl p-4 shadow-xl flex flex-col justify-between">
          <div>
            <div class="text-2xl mb-2">🧱</div>
            <h3 class="text-sm font-bold text-white mb-1">3 Codebases</h3>
            <p class="text-xs text-slate-300 leading-relaxed m-0">
              Rails Monolith + Swift (iOS) + Kotlin (Android).
            </p>
          </div>
        </div>

        <div class="bg-slate-900/90 border border-red-500/30 rounded-2xl p-4 shadow-xl flex flex-col justify-between">
          <div>
            <div class="text-2xl mb-2">👥</div>
            <h3 class="text-sm font-bold text-white mb-1">Tripled Engineering Team</h3>
            <p class="text-xs text-slate-300 leading-relaxed m-0">
              Requires dedicated iOS & Android engineers for simple updates.
            </p>
          </div>
        </div>

        <div class="bg-slate-900/90 border border-red-500/30 rounded-2xl p-4 shadow-xl flex flex-col justify-between">
          <div>
            <div class="text-2xl mb-2">📋</div>
            <h3 class="text-sm font-bold text-white mb-1">Duplicated Logic</h3>
            <p class="text-xs text-slate-300 leading-relaxed m-0">
              Form validations & business workflows must be written 3 times.
            </p>
          </div>
        </div>
      </div>

      <!-- Bottom Simple Callout -->
      <div class="p-3 bg-slate-950 border border-slate-800 rounded-xl text-left flex items-center justify-between">
        <span class="text-xs text-slate-300">💡 <strong>Verdict:</strong> 100% native performance, but unsustainable cost for small teams.</span>
        <span class="text-[10px] font-mono text-red-400">Level 3 Complexity</span>
      </div>
    </template>

    <!-- DEFAULT / ALL VIEW -->
    <template v-if="!approach || approach === 'all'">
      <div class="flex justify-between items-center mb-2">
        <span class="rails-badge">⚖️ Trade-off Analysis</span>
        <span class="text-xs font-mono text-slate-400">Evaluating Current Options</span>
      </div>

      <h2 class="text-2xl font-black tracking-tight text-white mb-4 text-left">
        Alternative Mobile Approaches & <span class="text-transparent bg-clip-text bg-gradient-to-r from-red-400 via-amber-300 to-red-500">Their Limitations</span>
      </h2>

      <div class="grid grid-cols-1 md:grid-cols-3 gap-3">
        <!-- PWA Card -->
        <div class="bg-slate-900/90 border border-amber-500/30 rounded-2xl p-4 text-left shadow-xl flex flex-col justify-between">
          <div>
            <div class="flex items-center justify-between border-b border-slate-800 pb-2 mb-2">
              <span class="text-sm font-bold text-white">1. PWAs 🌐</span>
              <span class="text-[9px] bg-amber-950 text-amber-300 px-1.5 py-0.5 rounded border border-amber-800 font-mono">Level 1</span>
            </div>
            <p class="text-xs text-slate-300">No App Store presence & iOS Safari limits.</p>
          </div>
        </div>

        <!-- React Native Card -->
        <div class="bg-slate-900/90 border border-orange-500/30 rounded-2xl p-4 text-left shadow-xl flex flex-col justify-between">
          <div>
            <div class="flex items-center justify-between border-b border-slate-800 pb-2 mb-2">
              <span class="text-sm font-bold text-white">2. React Native ⚛️</span>
              <span class="text-[9px] bg-orange-950 text-orange-300 px-1.5 py-0.5 rounded border border-orange-800 font-mono">Level 2</span>
            </div>
            <p class="text-xs text-slate-300">API endpoints & double state management.</p>
          </div>
        </div>

        <!-- Full Native Card -->
        <div class="bg-slate-900/90 border border-red-500/30 rounded-2xl p-4 text-left shadow-xl flex flex-col justify-between">
          <div>
            <div class="flex items-center justify-between border-b border-slate-800 pb-2 mb-2">
              <span class="text-sm font-bold text-white">3. Full Native 📱</span>
              <span class="text-[9px] bg-red-950 text-red-300 px-1.5 py-0.5 rounded border border-red-800 font-mono">Level 3</span>
            </div>
            <p class="text-xs text-slate-300">3 codebases & tripled engineering costs.</p>
          </div>
        </div>
      </div>
    </template>

  </div>
</template>

<script setup>
import { computed } from 'vue'

const props = defineProps({
  approach: {
    type: String,
    default: 'all' // 'pwa' | 'react-native' | 'native' | 'all'
  }
})

const currentStep = computed(() => {
  if (props.approach === 'pwa') return 1
  if (props.approach === 'react-native') return 2
  if (props.approach === 'native') return 3
  return 0
})

const complexityLabel = computed(() => {
  if (props.approach === 'pwa') return 'Level 1 / 3 (Low)'
  if (props.approach === 'react-native') return 'Level 2 / 3 (Medium)'
  if (props.approach === 'native') return 'Level 3 / 3 (High)'
  return 'Comparison'
})

const complexityBadgeStyle = computed(() => {
  if (props.approach === 'pwa') return 'bg-amber-950/80 border-amber-600 text-amber-300'
  if (props.approach === 'react-native') return 'bg-orange-950/80 border-orange-600 text-orange-300'
  if (props.approach === 'native') return 'bg-red-950/80 border-red-600 text-red-300'
  return 'bg-slate-900 border-slate-700 text-slate-300'
})
</script>
