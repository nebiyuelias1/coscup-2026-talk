<template>
  <div class="hotwire-detection-slide w-full my-auto flex flex-col justify-center">
    <!-- Header -->
    <h2 class="text-2xl font-black tracking-tight text-white mb-4 text-left">
      Detecting Native vs Web: <span class="text-red-500">hotwire_native_app? ⚡</span>
    </h2>

    <!-- 2 Column Grid Layout: Left Explanations, Right Code Snippet -->
    <div class="grid grid-cols-1 md:grid-cols-12 gap-4 items-center text-left">
      
      <!-- Left Column: Detection Flow Steps (Cols 1-5) -->
      <div class="md:col-span-5 space-y-3">
        <div class="bg-slate-900/90 border border-red-500/30 rounded-xl p-3.5 shadow-lg space-y-1">
          <h4 class="text-xs font-bold text-red-400 m-0">1. User-Agent Header</h4>
          <p class="text-[11px] text-slate-300 leading-snug m-0">
            Hotwire Native mobile shells send custom HTTP User-Agent headers.
          </p>
        </div>

        <div class="bg-slate-900/90 border border-amber-500/30 rounded-xl p-3.5 shadow-lg space-y-1">
          <h4 class="text-xs font-bold text-amber-400 m-0">2. hotwire_native_app? Helper</h4>
          <p class="text-[11px] text-slate-300 leading-snug m-0">
            Rails helper checks User-Agent and returns <code class="text-amber-300 font-mono">true</code> for mobile apps.
          </p>
        </div>

        <div class="bg-slate-900/90 border border-emerald-500/30 rounded-xl p-3.5 shadow-lg space-y-1">
          <h4 class="text-xs font-bold text-emerald-400 m-0">3. HTML Root Data Attribute</h4>
          <p class="text-[11px] text-slate-300 leading-snug m-0">
            Injects <code class="text-emerald-300 font-mono">data-hotwire-native</code> onto <code class="text-slate-200 font-mono">&lt;html&gt;</code> root element.
          </p>
        </div>
      </div>

      <!-- Right Column: Code Snippet (Cols 6-12) -->
      <div class="md:col-span-7 space-y-1.5">
        <div class="text-[11px] font-mono text-slate-400 px-1">
          app/views/layouts/application.html.erb
        </div>

        <div class="bg-slate-950 border border-slate-800 rounded-xl p-3.5 shadow-2xl font-mono text-[11px] text-slate-300 overflow-x-auto leading-relaxed space-y-2">
          <div class="text-slate-500 border-b border-slate-800 pb-1.5">
            &lt;!DOCTYPE html&gt;
          </div>

          <div class="bg-amber-950/40 p-2 rounded border border-amber-500/40 text-amber-300 font-bold">
            &lt;<span class="text-purple-400">html</span> data-theme=<span class="text-emerald-300">"silk"</span> <span class="text-red-400">&lt;%=</span> <span class="text-emerald-300">"data-hotwire-native"</span> <span class="text-purple-400">if</span> hotwire_native_app? <span class="text-red-400">%&gt;</span>&gt;
          </div>

          <div class="pl-4 text-slate-400 space-y-1 text-[10.5px]">
            <div>&lt;<span class="text-purple-400">head</span>&gt;</div>
            <div class="pl-4 text-emerald-400 font-bold">
              &lt;%= stylesheet_link_tag <span class="text-emerald-300">"native"</span> if hotwire_native_app? %&gt;
            </div>
            <div>&lt;/<span class="text-purple-400">head</span>&gt;</div>
            <br/>
            <div>&lt;<span class="text-purple-400">body</span> class=<span class="text-emerald-300">"bg-background text-content"</span>&gt;</div>
            <div class="pl-4 text-slate-300">&lt;%= render <span class="text-emerald-300">"shared/navbar"</span> %&gt;</div>
            <div class="pl-4 text-amber-300">&lt;%= yield %&gt;</div>
            <div>&lt;/<span class="text-purple-400">body</span>&gt;</div>
          </div>

          <div>&lt;/<span class="text-purple-400">html</span>&gt;</div>
        </div>
      </div>

    </div>
  </div>
</template>

<script setup>
</script>
