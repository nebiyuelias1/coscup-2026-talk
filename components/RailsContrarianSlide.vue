<template>
  <div
    class="rails-contrarian-slide w-full my-auto flex flex-col justify-center text-left"
  >
    <!-- Progress Indicator Bar for single pillar slides -->
    <div v-if="pillar && pillar !== 'all'" class="mb-2">
      <div class="flex items-center justify-between mb-1">
        <span class="rails-badge font-bold text-xs"
          >🥊 The Rails Philosophy</span
        >
        <span
          class="text-[11px] font-mono text-amber-300 bg-amber-950/80 px-2 py-0.5 rounded border border-amber-500/40"
        >
          Point {{ currentPillarIndex }} of 4 🎯
        </span>
      </div>

      <!-- 4-Segment Progress Bar -->
      <div class="grid grid-cols-4 gap-2">
        <div
          v-for="idx in [1, 2, 3, 4]"
          :key="idx"
          :class="[
            'h-1 rounded-full transition-all',
            idx <= currentPillarIndex
              ? 'bg-red-500 shadow-sm shadow-red-500/50'
              : 'bg-slate-800',
          ]"
        ></div>
      </div>
    </div>

    <!-- Header for Overview Slide -->
    <div v-else class="flex justify-between items-center mb-1">
      <span class="rails-badge font-bold text-xs">🥊 The Rails Philosophy</span>
      <span class="text-[11px] font-mono text-slate-400"
        >Pragmatism Over Hype</span
      >
    </div>

    <!-- Main Title -->
    <h2
      class="text-xl font-black tracking-tight text-white mb-3 flex items-center justify-between"
    >
      <span>Embrace Being <span class="text-red-500">Contrarian 🎯</span></span>
      <span
        v-if="!pillar || pillar === 'all'"
        class="text-[11px] font-mono text-amber-300 bg-amber-950/80 px-2 py-0.5 rounded border border-amber-500/40"
      >
        Simplicity > Hype ⚡
      </span>
    </h2>

    <!-- SINGLE PILLAR SLIDE VIEW -->

    <!-- Point 1: Solid Cache & Queue -->
    <template v-if="pillar === 'solid'">
      <div
        class="bg-slate-900/90 border-2 border-red-500/40 rounded-xl p-4 shadow-xl space-y-2.5"
      >
        <div
          class="flex items-center justify-between border-b border-slate-800 pb-2"
        >
          <div class="flex items-center gap-2.5">
            <span class="text-2xl">🗄️</span>
            <div>
              <h3 class="text-lg font-black text-white m-0">
                1. Solid Cache & Solid Queue
              </h3>
              <p class="text-[11px] text-red-400 font-mono m-0">
                Database as Infrastructure
              </p>
            </div>
          </div>
        </div>

        <div class="p-2.5 bg-slate-950/80 border border-slate-800 rounded-lg">
          <p class="text-xs text-slate-300 line-through m-0">
            "You must run Redis, Memcached, and complex RAM server clusters just
            for caching and background jobs."
          </p>
        </div>

        <div class="p-3 bg-red-950/40 border border-red-500/30 rounded-lg">
          <p class="text-xs text-slate-100 leading-relaxed m-0 font-medium">
            Use your existing SQL database for caching (SolidCache) and
            background jobs (SolidQueue). Zero extra RAM clusters, zero extra
            DevOps maintenance.
          </p>
        </div>
      </div>
    </template>

    <!-- Point 2: Schema Introspection -->
    <template v-if="pillar === 'schema'">
      <div
        class="bg-slate-900/90 border-2 border-amber-500/40 rounded-xl p-4 shadow-xl space-y-2.5"
      >
        <div
          class="flex items-center justify-between border-b border-slate-800 pb-2"
        >
          <div class="flex items-center gap-2.5">
            <span class="text-2xl">🔍</span>
            <div>
              <h3 class="text-lg font-black text-white m-0">
                2. Schema Introspection
              </h3>
              <p class="text-[11px] text-amber-400 font-mono m-0">
                ActiveRecord Runtime Magic
              </p>
            </div>
          </div>
        </div>

        <div class="p-2.5 bg-slate-950/80 border border-slate-800 rounded-lg">
          <p class="text-xs text-slate-300 line-through m-0">
            "Manually define, duplicate, and sync every database model property
            across ORMs, DTOs, and type definitions."
          </p>
        </div>

        <div class="p-3 bg-amber-950/40 border border-amber-500/30 rounded-lg">
          <p class="text-xs text-slate-100 leading-relaxed m-0 font-medium">
            ActiveRecord inspects the database schema automatically at boot
            time. Zero boilerplate model declarations, zero schema drift, and
            maximum developer efficiency.
          </p>
        </div>
      </div>
    </template>

    <!-- Point 3: Majestic Monolith -->
    <template v-if="pillar === 'monolith'">
      <div
        class="bg-slate-900/90 border-2 border-purple-500/40 rounded-xl p-4 shadow-xl space-y-2.5"
      >
        <div
          class="flex items-center justify-between border-b border-slate-800 pb-2"
        >
          <div class="flex items-center gap-2.5">
            <span class="text-2xl">🏰</span>
            <div>
              <h3 class="text-lg font-black text-white m-0">
                3. Majestic Monolith
              </h3>
              <p class="text-[11px] text-purple-300 font-mono m-0">
                1 Developer Powerhouse
              </p>
            </div>
          </div>
        </div>

        <div class="p-2.5 bg-slate-950/80 border border-slate-800 rounded-lg">
          <p class="text-xs text-slate-300 line-through m-0">
            "Split your early app into 50 Kubernetes microservices with
            distributed tracing and API gateways."
          </p>
        </div>

        <div
          class="p-3 bg-purple-950/40 border border-purple-500/30 rounded-lg"
        >
          <p class="text-xs text-slate-100 leading-relaxed m-0 font-medium">
            One cohesive Rails monolith contains all your business logic. 1
            developer can build, test, and deploy features in minutes instead of
            waiting on cross-team coordination.
          </p>
        </div>
      </div>
    </template>

    <!-- Point 4: HTML Over The Wire -->
    <template v-if="pillar === 'hotwire'">
      <div
        class="bg-slate-900/90 border-2 border-emerald-500/40 rounded-xl p-4 shadow-xl space-y-2.5"
      >
        <div
          class="flex items-center justify-between border-b border-slate-800 pb-2"
        >
          <div class="flex items-center gap-2.5">
            <span class="text-2xl">⚡</span>
            <div>
              <h3 class="text-lg font-black text-white m-0">
                4. HTML Over The Wire (Hotwire)
              </h3>
              <p class="text-[11px] text-emerald-400 font-mono m-0">
                Web + Mobile Unified
              </p>
            </div>
          </div>
        </div>

        <div class="p-2.5 bg-slate-950/80 border border-slate-800 rounded-lg">
          <p class="text-xs text-slate-300 line-through m-0">
            "Build separate SPA frontend apps, REST API layers, and rewrite all
            UI components natively for iOS & Android."
          </p>
        </div>

        <div
          class="p-3 bg-emerald-950/40 border border-emerald-500/30 rounded-lg"
        >
          <p class="text-xs text-slate-100 leading-relaxed m-0 font-medium">
            Render HTML on the server and stream directly inside native mobile
            shells. Power your Web app, iOS app, and Android app simultaneously
            from 1 Rails codebase!
          </p>
        </div>
      </div>
    </template>

    <!-- OVERVIEW SLIDE (Pillar == 'all' or default) -->
    <template v-if="!pillar || pillar === 'all'">
      <div class="grid grid-cols-1 md:grid-cols-2 gap-2.5 mb-2.5 text-left">
        <!-- 1. Solid Cache / Queue -->
        <div
          class="bg-slate-900/90 border border-red-500/30 rounded-xl p-3 shadow-lg flex flex-col justify-between"
        >
          <div>
            <div class="flex items-center justify-between mb-1">
              <span
                class="text-xs font-bold text-red-400 flex items-center gap-1"
              >
                🗄️ Solid Cache & Queue
              </span>
              <span
                class="text-[9px] font-mono bg-red-950 text-red-300 px-1.5 py-0.5 rounded border border-red-800"
              >
                Database as Infra
              </span>
            </div>
            <p class="text-[11px] text-slate-200 leading-snug m-0">
              Use SQL database for cache & background jobs (SolidCache /
              SolidQueue).
            </p>
          </div>
        </div>

        <!-- 2. ActiveRecord Introspection -->
        <div
          class="bg-slate-900/90 border border-amber-500/30 rounded-xl p-3 shadow-lg flex flex-col justify-between"
        >
          <div>
            <div class="flex items-center justify-between mb-1">
              <span
                class="text-xs font-bold text-amber-400 flex items-center gap-1"
              >
                🔍 Schema Introspection
              </span>
              <span
                class="text-[9px] font-mono bg-amber-950 text-amber-300 px-1.5 py-0.5 rounded border border-amber-800"
              >
                Zero Boilerplate
              </span>
            </div>
            <p class="text-[11px] text-slate-200 leading-snug m-0">
              ActiveRecord inspects database schema automatically at runtime.
            </p>
          </div>
        </div>

        <!-- 3. Majestic Monolith -->
        <div
          class="bg-slate-900/90 border border-purple-500/30 rounded-xl p-3 shadow-lg flex flex-col justify-between"
        >
          <div>
            <div class="flex items-center justify-between mb-1">
              <span
                class="text-xs font-bold text-purple-300 flex items-center gap-1"
              >
                🏰 Majestic Monolith
              </span>
              <span
                class="text-[9px] font-mono bg-purple-950 text-purple-300 px-1.5 py-0.5 rounded border border-purple-800"
              >
                Solo Dev Speed
              </span>
            </div>
            <p class="text-[11px] text-slate-200 leading-snug m-0">
              One cohesive codebase powers your entire web & mobile product.
            </p>
          </div>
        </div>

        <!-- 4. HTML Over The Wire -->
        <div
          class="bg-slate-900/90 border border-emerald-500/30 rounded-xl p-3 shadow-lg flex flex-col justify-between"
        >
          <div>
            <div class="flex items-center justify-between mb-1">
              <span
                class="text-xs font-bold text-emerald-400 flex items-center gap-1"
              >
                ⚡ HTML Over The Wire
              </span>
              <span
                class="text-[9px] font-mono bg-emerald-950 text-emerald-300 px-1.5 py-0.5 rounded border border-emerald-800"
              >
                Hotwire Native
              </span>
            </div>
            <p class="text-[11px] text-slate-200 leading-snug m-0">
              Render HTML on server & stream directly inside native mobile
              shells.
            </p>
          </div>
        </div>
      </div>
    </template>
  </div>
</template>

<script setup>
import { computed } from "vue";

const props = defineProps({
  pillar: {
    type: String,
    default: null,
  },
});

const currentPillarIndex = computed(() => {
  switch (props.pillar) {
    case "solid":
      return 1;
    case "schema":
      return 2;
    case "monolith":
      return 3;
    case "hotwire":
      return 4;
    default:
      return 0;
  }
});
</script>
