---
theme: default
background: https://cover.sli.dev
title: Building Native Mobile Apps Using Rails
info: |
  ## Building Native Mobile Apps Using Rails
  COSCUP 2026 Presentation by Nebiyu Elias Talefe
class: text-center ruby-hero
drawings:
  persist: false
transition: slide-left
comark: true
duration: 30min
style: |
  .slidev-layout {
    background: radial-gradient(circle at 50% 20%, rgba(204, 0, 0, 0.25) 0%, transparent 60%),
                radial-gradient(circle at 80% 80%, rgba(157, 78, 221, 0.15) 0%, transparent 50%),
                #0F0D13 !important;
  }
---

<div class="flex flex-col items-center justify-center h-full px-4">
  
  <div class="flex items-center gap-2.5 mb-4 flex-wrap justify-center">
    <span class="rails-badge">💎 Ruby on Rails</span>
    <span class="hotwire-badge">⚡ Hotwire Native</span>
    <div class="title-chip flex items-center gap-1.5">
      <img src="/ruby_taiwan_logo.svg" alt="Ruby Taiwan Logo" class="h-4.5 object-contain" />
      <img src="/ruby_taiwan_logotype.svg" alt="Ruby Taiwan" class="h-3.5 object-contain filter invert brightness-200" />
    </div>
    <div class="title-chip">
      <img src="/coscup_logo.png" alt="COSCUP Logo" class="h-3.5 object-contain" />
      <span>COSCUP 2026</span>
    </div>
  </div>

  <h1 class="text-5xl font-extrabold tracking-tight mb-4">
    Building Native Mobile Apps<br>
    <span class="text-red-500">
      Using Rails
    </span>
  </h1>

  <p class="text-xl text-slate-300 max-w-2xl mx-auto font-medium mb-8">
    How to ship production iOS & Android apps at 5x speed using Hotwire Native, Strada, and your existing Rails backend.
  </p>

  <div class="flex items-center justify-center gap-3 text-sm font-semibold flex-wrap">
    <div class="flex items-center gap-2 bg-slate-900/80 px-4 py-2 rounded-xl border border-red-500/30">
      <span class="w-2.5 h-2.5 rounded-full bg-red-500 animate-pulse"></span>
      <span class="text-white">Speaker:</span>
      <span class="text-red-400 font-bold">Nebiyu Elias Talefe</span>
    </div>
    <div class="bg-slate-900/80 px-4 py-2 rounded-xl border border-slate-700 text-slate-300 font-mono text-xs flex items-center gap-1.5">
      <span>📅 Aug 8, 2026</span>
    </div>
    <div class="bg-slate-900/80 px-4 py-2 rounded-xl border border-slate-700 text-slate-300 font-mono text-xs flex items-center gap-1.5">
      <span>📍 NTUST, Taipei, Taiwan</span>
    </div>
  </div>

</div>

---
transition: fade-out
layout: default
---

<div class="flex justify-between items-center mb-2">
  <span class="rails-badge">👨‍💻 About The Speaker</span>
  <span class="text-xs font-mono text-slate-400">COSCUP 2026</span>
</div>

# Hi, I'm Neba 👋 🇪🇹

<SpeakerCard />

<div class="grid grid-cols-4 gap-3 mt-3 text-xs">
  <div class="p-3 bg-slate-900/70 rounded-xl border border-slate-800">
    <div class="text-red-400 font-bold text-sm mb-1">🚀 7+ Years Experience</div>
    <p class="text-slate-300 m-0">Full-stack engineer building web & mobile applications.</p>
  </div>
  <div class="p-3 bg-slate-900/70 rounded-xl border border-slate-800">
    <div class="text-amber-400 font-bold text-sm mb-1">🏢 Currently @ ASUS</div>
    <p class="text-slate-300 m-0">Building modern web and mobile product experiences.</p>
  </div>
  <div class="p-3 bg-slate-900/70 rounded-xl border border-slate-800">
    <div class="text-emerald-400 font-bold text-sm mb-1">🤝 Co-op @ 508.dev</div>
    <p class="text-slate-300 m-0">Member of software engineer co-operative 508.dev.</p>
  </div>
  <div class="p-3 bg-slate-900/70 rounded-xl border border-cyan-800/60">
    <div class="text-cyan-400 font-bold text-sm mb-1">🐧 OS & Setup</div>
    <p class="text-slate-300 m-0 font-mono text-[11px]">I use omarchy btw</p>
  </div>
</div>

---
transition: slide-up
layout: default
---

<MobileRequirementSlide />

---
transition: slide-up
layout: default
---

<AlternativesSlide approach="pwa" />

---
transition: slide-up
layout: default
---

<AlternativesSlide approach="react-native" />

---
transition: slide-up
layout: default
---

<ReactNativeCaseStudySlide />

---
transition: slide-up
layout: default
---

<AlternativesSlide approach="native" />

---
transition: slide-up
layout: default
---

<SmallTeamIdeaSlide />

---
transition: slide-up
layout: default
---

<WebviewMythsSlide />

---
transition: slide-up
layout: default
---

<RailsContrarianSlide pillar="solid" />

---
transition: slide-up
layout: default
---

<RailsContrarianSlide pillar="schema" />

---
transition: slide-up
layout: default
---

<RailsContrarianSlide pillar="monolith" />

---
transition: slide-up
layout: default
---

<RailsContrarianSlide pillar="hotwire" />

---
transition: slide-left
layout: default
---

<HotwireNativeIntroSlide />

---
transition: slide-left
layout: default
---

<WhatIsHotwireNativeSlide />

---
transition: slide-left
layout: default
---

<MonorepoSetupSlide />

---
transition: slide-left
layout: default
---

<HotwireIosSetupSlide />

---
transition: slide-left
layout: default
---

<HotwireAndroidSetupSlide />

---
transition: slide-left
layout: default
---

<CrossPlatformResultSlide />

---
transition: slide-left
layout: default
---

<HotwireDetectionSlide />

---
transition: slide-left
layout: default
---

<TailwindNativeHidingSlide />

---
transition: slide-left
layout: default
---

<DynamicNativeTitleSlide />

---
transition: slide-left
layout: default
---

<LiveDemoSlide />

---
transition: slide-left
layout: default
---

<HotwireInteractionSlide />

---
transition: slide-left
layout: default
---

<div class="flex justify-between items-center mb-2">
  <span class="rails-badge">💻 Rails Code</span>
  <span class="text-xs font-mono text-slate-400">app/controllers/posts_controller.rb</span>
</div>

# 1. Server-Driven Rails Views 💎

One Rails Controller serves your Web app and Native Mobile app seamlessly:

```ruby {all|4-8|10-15}
class PostsController < ApplicationController
  before_action :authenticate_user!

  def index
    @posts = Post.order(created_at: :desc)
    # Serves HTML to both Web browser and Hotwire Native iOS/Android clients!
    render :index
  end

  def create
    @post = current_user.posts.build(post_params)
    if @post.save
      respond_to do |format|
        format.html { redirect_to @post, notice: "Post published!" }
        format.turbo_stream # Live update mobile feed!
      end
    end
  end
end
```

<div class="mt-3 p-3 bg-slate-950 rounded-lg border border-slate-800 text-xs text-left">
  💡 <strong class="text-red-400">Pro Tip:</strong> Use `hotwire_native_app?` in ERB helpers to tweak mobile-specific layouts or hide web header bars!
</div>

---
transition: slide-up
layout: default
---

<div class="flex justify-between items-center mb-2">
  <span class="hotwire-badge">⚙️ Config</span>
  <span class="text-xs font-mono text-slate-400">path_configuration.json</span>
</div>

# 2. Native Navigation Stack Config 🗺️

Control native iOS/Android navigation behavior **from your Rails server** dynamically!

```json {all|3-10|12-22}
{
  "settings": {
    "tabs": [
      { "title": "Feed", "url": "/", "icon": "house" },
      { "title": "Explore", "url": "/explore", "icon": "magnifyingglass" },
      { "title": "Notifications", "url": "/notifications", "icon": "bell" },
      { "title": "Profile", "url": "/profile", "icon": "person" }
    ]
  },
  "rules": [
    {
      "patterns": ["/posts/new$", "/settings$"],
      "properties": {
        "presentation": "modal"
      }
    },
    {
      "patterns": ["/login$"],
      "properties": {
        "presentation": "clear_all"
      }
    }
  ]
}
```

---
transition: slide-left
layout: default
---

<div class="flex justify-between items-center mb-2">
  <span class="rails-badge">🌉 Strada</span>
  <span class="text-xs font-mono text-slate-400">HTML to Native Bridge</span>
</div>

# 3. Leveling Up with Strada ⚡

Strada bridges web HTML elements to native Swift (iOS) and Kotlin (Android) components.

<StradaVisualizer />

<div class="grid grid-cols-2 gap-4 mt-3 text-left">
<div>
  <div class="font-bold text-red-400 text-xs mb-1">HTML View (ERB)</div>

```html
<form data-controller="bridge--form" data-bridge--form-title-value="Save Post">
  <!-- Rails Form Fields -->
</form>
```

</div>

<div>
  <div class="font-bold text-purple-400 text-xs mb-1">Native Swift Component</div>

```swift
class FormComponent: BridgeComponent {
  override class var name: String { "form" }
  // Renders native iOS bar submit button!
}
```

</div>
</div>

---
transition: fade-out
layout: default
---

<div class="flex justify-between items-center mb-2">
  <span class="rails-badge">📊 Comparison</span>
  <span class="text-xs font-mono text-slate-400">Why Hotwire Native Wins</span>
</div>

# React Native vs Rails + Hotwire Native ⚔️

<ComparisonMatrix />

<div class="p-3 bg-red-950/40 border border-red-500/30 rounded-xl text-center text-xs text-red-200 font-medium">
  🚀 <strong>Result:</strong> 1 developer can build and ship what traditionally required a 5-person mobile + backend team!
</div>

---
transition: slide-up
layout: default
---

<div class="flex justify-between items-center mb-2">
  <span class="rails-badge">⭐ Starter Template</span>
  <span class="text-xs font-mono text-slate-400">Open Source</span>
</div>

# Nebiyu's Rails Mobile Starter Template 🛠️

I built an open-source starter template so you can launch your mobile Rails app today:

<div class="bg-slate-900/90 border border-amber-500/40 rounded-2xl p-5 text-left my-3 shadow-xl">
  <div class="flex items-center justify-between border-b border-slate-800 pb-3 mb-3">
    <div class="flex items-center gap-3">
      <div class="w-10 h-10 rounded-xl bg-red-600 flex items-center justify-center text-xl font-bold text-white shadow">
        🚀
      </div>
      <div>
        <h3 class="text-lg font-black text-white m-0">turbo-rails-react-native-starter</h3>
        <p class="text-xs text-amber-400 font-mono m-0">github.com/nebiyuelias1/turbo-rails-react-native-starter</p>
      </div>
    </div>
    <span class="px-3 py-1 bg-amber-500/20 text-amber-300 border border-amber-500/40 rounded-full text-xs font-bold">
      ⭐ Star on GitHub
    </span>
  </div>

  <div class="grid grid-cols-2 gap-4 text-xs">
    <div class="space-y-1.5 text-slate-300">
      <div>✅ <strong>Pre-configured Auth:</strong> Devise + Session tokens</div>
      <div>✅ <strong>Native iOS and Android:</strong> Ready to build</div>
      <div>✅ <strong>Strada Bridges:</strong> Form and Haptic bridges</div>
    </div>
    <div class="space-y-1.5 text-slate-300">
      <div>✅ <strong>Dark Mode:</strong> Tailwind CSS and CSS variables</div>
      <div>✅ <strong>Turbo Streams:</strong> WebSocket and ActionCable</div>
      <div>✅ <strong>CI/CD:</strong> GitHub Actions workflow included</div>
    </div>
  </div>
</div>

```bash
git clone https://github.com/nebiyuelias1/turbo-rails-react-native-starter.git
cd turbo-rails-react-native-starter && bundle install
bin/rails s
```

---
transition: slide-left
layout: default
---

<div class="flex justify-between items-center mb-2">
  <span class="rails-badge">🎯 Best Practices</span>
  <span class="text-xs font-mono text-slate-400">Production Playbook</span>
</div>

# Lessons from Building Hotwire Apps 🧠

<div class="grid grid-cols-2 gap-4 text-left mt-4">
  
  <div class="p-4 bg-slate-900/80 rounded-xl border border-slate-800">
    <h4 class="text-sm font-bold text-red-400 mb-2">1. Cache Strategy and Speed</h4>
    <p class="text-xs text-slate-300 m-0 leading-relaxed">
      Use Turbo cache snapshots for instant page restores. Serve static assets via CDN and leverage HTTP caching headers for lightning-fast screen transitions.
    </p>
  </div>

  <div class="p-4 bg-slate-900/80 rounded-xl border border-slate-800">
    <h4 class="text-sm font-bold text-blue-400 mb-2">2. When to Go Native</h4>
    <p class="text-xs text-slate-300 m-0 leading-relaxed">
      Keep 90% of screens as web HTML. Build Strada components for heavy native features like camera capture, barcode scanning, biometrics, or real-time maps.
    </p>
  </div>

  <div class="p-4 bg-slate-900/80 rounded-xl border border-slate-800">
    <h4 class="text-sm font-bold text-purple-400 mb-2">3. Offline Experience</h4>
    <p class="text-xs text-slate-300 m-0 leading-relaxed">
      Handle offline fallback screens natively with custom offline HTML pages embedded in your iOS and Android app bundles.
    </p>
  </div>

  <div class="p-4 bg-slate-900/80 rounded-xl border border-slate-800">
    <h4 class="text-sm font-bold text-amber-400 mb-2">4. App Store Compliance</h4>
    <p class="text-xs text-slate-300 m-0 leading-relaxed">
      Apple and Google fully support Hotwire Native apps (Basecamp and HEY have millions of users). Ensure native Apple Pay / IAP for digital goods if required.
    </p>
  </div>

</div>

---
transition: fade-out
class: text-center ruby-hero
---

<WrapUpSlide />

---
transition: slide-up
class: text-center ruby-hero
---

<PortfolioTalksSlide />
