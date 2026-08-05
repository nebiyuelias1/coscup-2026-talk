<template>
  <div
    class="hotwire-android-setup-slide w-full my-auto flex flex-col justify-center"
  >
    <!-- Header -->
    <div class="flex justify-between items-center mb-1">
      <span class="hotwire-badge font-bold">🤖 Android Integration</span>
      <span class="text-xs font-mono text-slate-400">Kotlin SDK</span>
    </div>

    <h2
      class="text-2xl font-black tracking-tight text-white mb-2 text-left flex items-center justify-between"
    >
      <span
        >Adding Hotwire Native to Android
        <span class="text-emerald-400">(Kotlin) 🤖</span></span
      >

      <!-- Stepper Controls -->
      <div class="flex items-center gap-1.5 font-mono text-xs">
        <button
          v-for="step in [1, 2, 3]"
          :key="step"
          @click="activeStep = step"
          :class="[
            'px-2.5 py-1 rounded-lg border transition-all flex items-center gap-1 font-bold',
            activeStep === step
              ? 'bg-emerald-950/80 border-emerald-500 text-emerald-300 shadow-lg scale-105 ring-1 ring-emerald-500/50'
              : 'bg-slate-900 border-slate-800 text-slate-400 hover:text-white',
          ]"
        >
          Step {{ step }}
        </button>
      </div>
    </h2>

    <!-- 2 Column Grid Layout: Left Setup Steps, Right Focused Code Snippet -->
    <div class="grid grid-cols-1 md:grid-cols-12 gap-4 items-center text-left">
      <!-- Left Column: Setup Steps (Cols 1-5) -->
      <div class="md:col-span-5 space-y-2.5">
        <!-- Step 1 Card -->
        <div
          @click="activeStep = 1"
          :class="[
            'p-3 rounded-xl border transition-all cursor-pointer relative overflow-hidden',
            activeStep === 1
              ? 'bg-slate-900 border-emerald-500/60 shadow-lg ring-1 ring-emerald-500/40 translate-x-1'
              : 'bg-slate-900/60 border-slate-800 opacity-70 hover:opacity-100',
          ]"
        >
          <div class="flex items-start gap-2.5">
            <span
              :class="[
                'w-6 h-6 rounded-lg flex items-center justify-center font-bold text-xs shrink-0',
                activeStep === 1
                  ? 'bg-emerald-500/20 text-emerald-400 border border-emerald-500/40'
                  : 'bg-slate-800 text-slate-400',
              ]"
              >1</span
            >
            <div>
              <h4 class="text-xs font-bold text-white m-0">
                1. Set Base Server URL
              </h4>
              <p class="text-[11px] text-slate-300 leading-snug m-0 mt-0.5">
                Define your Rails app production URL endpoint.
              </p>
            </div>
          </div>
        </div>

        <!-- Step 2 Card -->
        <div
          @click="activeStep = 2"
          :class="[
            'p-3 rounded-xl border transition-all cursor-pointer relative overflow-hidden',
            activeStep === 2
              ? 'bg-slate-900 border-amber-500/60 shadow-lg ring-1 ring-amber-500/40 translate-x-1'
              : 'bg-slate-900/60 border-slate-800 opacity-70 hover:opacity-100',
          ]"
        >
          <div class="flex items-start gap-2.5">
            <span
              :class="[
                'w-6 h-6 rounded-lg flex items-center justify-center font-bold text-xs shrink-0',
                activeStep === 2
                  ? 'bg-amber-500/20 text-amber-300 border border-amber-500/40'
                  : 'bg-slate-800 text-slate-400',
              ]"
              >2</span
            >
            <div>
              <h4 class="text-xs font-bold text-white m-0">
                2. Subclass HotwireActivity
              </h4>
              <p class="text-[11px] text-slate-300 leading-snug m-0 mt-0.5">
                Extend
                <code class="text-amber-300 font-mono">HotwireActivity</code> in
                your
                <code class="text-slate-200 font-mono">MainActivity.kt</code>.
              </p>
            </div>
          </div>
        </div>

        <!-- Step 3 Card -->
        <div
          @click="activeStep = 3"
          :class="[
            'p-3 rounded-xl border transition-all cursor-pointer relative overflow-hidden',
            activeStep === 3
              ? 'bg-slate-900 border-blue-500/60 shadow-lg ring-1 ring-blue-500/40 translate-x-1'
              : 'bg-slate-900/60 border-slate-800 opacity-70 hover:opacity-100',
          ]"
        >
          <div class="flex items-start gap-2.5">
            <span
              :class="[
                'w-6 h-6 rounded-lg flex items-center justify-center font-bold text-xs shrink-0',
                activeStep === 3
                  ? 'bg-blue-500/20 text-blue-400 border border-blue-500/40'
                  : 'bg-slate-800 text-slate-400',
              ]"
              >3</span
            >
            <div>
              <h4 class="text-xs font-bold text-white m-0">
                3. Configure Navigator Location
              </h4>
              <p class="text-[11px] text-slate-300 leading-snug m-0 mt-0.5">
                Set
                <code class="text-blue-300 font-mono">startLocation</code> in
                <code class="text-blue-300 font-mono"
                  >NavigatorConfiguration</code
                >.
              </p>
            </div>
          </div>
        </div>
      </div>

      <!-- Right Column: Real MainActivity.kt Code Snippet (Cols 6-12) -->
      <div class="md:col-span-7 space-y-1.5">
        <div
          class="flex items-center justify-between text-[11px] font-mono text-slate-400 px-1"
        >
          <span class="text-emerald-400 font-bold"
            >android/app/src/main/java/et/netale/litloop/MainActivity.kt</span
          >
          <span
            class="bg-slate-900 text-emerald-300 px-2 py-0.5 rounded text-[10px] border border-slate-800 font-bold"
            >Step {{ activeStep }} of 3</span
          >
        </div>

        <div
          class="bg-slate-950 border border-slate-800 rounded-xl p-3.5 shadow-2xl font-mono text-[11px] text-slate-300 overflow-x-auto leading-relaxed space-y-1 relative"
        >
          <!-- Package & Imports (Dimmed) -->
          <div
            :class="[
              'transition-opacity duration-300',
              activeStep ? 'opacity-40' : '',
            ]"
          >
            <span class="text-purple-400">package</span>
            <span class="text-emerald-300">et.netale.litloop</span><br />
            <span class="text-purple-400">import</span>
            <span class="text-amber-300"
              >dev.hotwire.navigation.activities.HotwireActivity</span
            ><br />
            <span class="text-purple-400">import</span>
            <span class="text-amber-300"
              >dev.hotwire.navigation.navigator.NavigatorConfiguration</span
            >
          </div>

          <!-- Step 1: Base URL Line -->
          <div
            :class="[
              'p-1.5 rounded transition-all duration-300',
              activeStep === 1
                ? 'bg-emerald-500/20 border-l-4 border-emerald-400 text-white font-bold shadow-lg ring-1 ring-emerald-500/30'
                : 'opacity-30',
            ]"
          >
            <span class="text-purple-400">const val</span> baseURL =
            <span class="text-emerald-300">"https://litloop.club"</span>
          </div>

          <!-- Step 2: Class Subclass Line -->
          <div
            :class="[
              'p-1.5 rounded transition-all duration-300',
              activeStep === 2
                ? 'bg-amber-500/20 border-l-4 border-amber-400 text-white font-bold shadow-lg ring-1 ring-amber-500/30'
                : 'opacity-30',
            ]"
          >
            <span class="text-purple-400">class</span>
            <span class="text-amber-300"> MainActivity</span> :
            <span class="text-emerald-300">HotwireActivity</span>() {
          </div>

          <!-- Method declaration (Dimmed) -->
          <div
            :class="[
              'transition-opacity duration-300 pl-4',
              activeStep ? 'opacity-40' : '',
            ]"
          >
            <span class="text-purple-400">override fun</span>
            <span class="text-blue-300">navigatorConfigurations</span>():
            List&lt;NavigatorConfiguration&gt; = listOf(
          </div>

          <!-- Step 3: Navigator Configuration Line -->
          <div
            :class="[
              'p-1.5 rounded transition-all duration-300 pl-8',
              activeStep === 3
                ? 'bg-blue-500/20 border-l-4 border-blue-400 text-white font-bold shadow-lg ring-1 ring-blue-500/30'
                : 'opacity-30',
            ]"
          >
            <span class="text-amber-300">NavigatorConfiguration</span>(<br />
            &nbsp;&nbsp;name = <span class="text-emerald-300">"main"</span>,
            startLocation = <span class="text-emerald-300">"$baseURL"</span>,
            navigatorHostId = <span class="text-blue-300">R.id.main</span><br />
            )
          </div>

          <div
            :class="[
              'transition-opacity duration-300 pl-4',
              activeStep ? 'opacity-40' : '',
            ]"
          >
            )
          </div>
          <div
            :class="[
              'transition-opacity duration-300',
              activeStep ? 'opacity-40' : '',
            ]"
          >
            }
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue";

const activeStep = ref(1);
</script>
