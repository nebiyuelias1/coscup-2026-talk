<template>
  <div class="small-team-idea-slide w-full my-auto flex flex-col justify-center">
    <!-- Header -->
    <div class="flex justify-between items-center mb-2">
      <span class="rails-badge font-bold">{{ currentLang === 'zh' ? '💡 靈光一閃' : '💡 The Lightbulb Moment' }}</span>
      <span class="text-xs font-mono text-slate-400">{{ currentLang === 'zh' ? '小團隊策略' : 'Small Team Strategy' }}</span>
    </div>

    <h2 class="text-3xl font-black tracking-tight text-white mb-3 text-left">
      <template v-if="currentLang === 'zh'">
        等等... 我們是 <span class="text-red-500">小團隊！ 🚀</span>
      </template>
      <template v-else>
        But Wait... We're a <span class="text-red-500">Small Team! 🚀</span>
      </template>
    </h2>

    <p class="text-sm text-slate-300 text-left mb-5">
      {{ currentLang === 'zh'
        ? '如果我們能直接利用「現有的 Rails Web App」來構建我們的原生手機 App 呢？'
        : 'What if we can use the Rails app we already have to also build our mobile app?' }}
    </p>
  </div>
</template>

<script setup>
import { currentLang } from '../composables/useLang'
</script>
