(() => {
  const STORAGE_KEY = "zs-site-mode";
  const DEFAULT_SITE_MODE = "external";
  const SITE_MODES = new Set(["internal", "external"]);
  const PAGE_MODES = new Set(["both", "internal", "external"]);
  const root = document.documentElement;
  const manifest = window.__ZS_SITE_MODE_MANIFEST__ || {};
  const currentPageMode = normalizePageMode(window.__ZS_PAGE_MODE__);

  function normalizeSiteMode(value) {
    return SITE_MODES.has(value) ? value : DEFAULT_SITE_MODE;
  }

  function normalizePageMode(value) {
    return PAGE_MODES.has(value) ? value : "both";
  }

  function getStoredMode() {
    try {
      return normalizeSiteMode(localStorage.getItem(STORAGE_KEY));
    } catch (error) {
      return DEFAULT_SITE_MODE;
    }
  }

  function storeMode(mode) {
    try {
      localStorage.setItem(STORAGE_KEY, mode);
    } catch (error) {}
  }

  function applyMode(mode) {
    root.dataset.zsMode = mode;
    root.dataset.zsPageMode = currentPageMode;
    updateToggleButtons(mode);
  }

  function updateToggleButtons(mode) {
    const isInternal = mode === "internal";

    document.querySelectorAll(".js-site-mode").forEach((button) => {
      button.setAttribute("aria-pressed", isInternal ? "true" : "false");
      button.setAttribute(
        "aria-label",
        isInternal ? button.dataset.ariaInternal || "Switch to external mode" : button.dataset.ariaExternal || "Switch to internal mode",
      );
      button.dataset.state = mode;
    });
  }

  function normalizeManifestPath(href) {
    if (!href) {
      return null;
    }

    let rootUrl;
    let targetUrl;

    try {
      rootUrl = new URL(root.dataset.contentRoot || "./", window.location.href);
      targetUrl = new URL(href, window.location.href);
    } catch (error) {
      return null;
    }

    if (rootUrl.protocol !== targetUrl.protocol) {
      return null;
    }

    if (rootUrl.protocol !== "file:" && rootUrl.origin !== targetUrl.origin) {
      return null;
    }

    const rootPath = rootUrl.pathname.endsWith("/") ? rootUrl.pathname : `${rootUrl.pathname}/`;
    if (!targetUrl.pathname.startsWith(rootPath)) {
      return null;
    }

    let relativePath = decodeURIComponent(targetUrl.pathname.slice(rootPath.length));
    if (!relativePath) {
      relativePath = "index.html";
    }

    return relativePath;
  }

  function findModeContainer(anchor) {
    return (
      anchor.closest(".sd-col") ||
      anchor.closest(".navigation-prev") ||
      anchor.closest(".navigation-next") ||
      anchor.closest(".globaltoc li") ||
      anchor.closest(".toctree-wrapper li") ||
      anchor.closest(".sy-breadcrumbs li") ||
      anchor.closest(".sy-head-links li") ||
      anchor.closest(".sy-head-extra li")
    );
  }

  function annotateConditionalLinks() {
    const selectors = [
      ".globaltoc a[href]",
      ".toctree-wrapper a[href]",
      ".sd-card a[href]",
      ".navigation a[href]",
      ".sy-breadcrumbs a[href]",
      ".sy-head-links a[href]",
    ];
    const containers = new Set();

    document.querySelectorAll(selectors.join(",")).forEach((anchor) => {
      const path = normalizeManifestPath(anchor.getAttribute("href"));
      if (!path) {
        return;
      }

      const targetMode = normalizePageMode(manifest[path]);
      if (targetMode === "both") {
        return;
      }

      const container = findModeContainer(anchor);
      if (!container) {
        return;
      }

      containers.add(container);
      container.classList.add(`zs-mode-target-${targetMode}`);
    });

    return containers;
  }

  function bindToggleButtons() {
    document.querySelectorAll(".js-site-mode").forEach((button) => {
      button.addEventListener("click", () => {
        const nextMode = root.dataset.zsMode === "internal" ? "external" : "internal";
        storeMode(nextMode);
        applyMode(nextMode);
      });
    });
  }

  applyMode(getStoredMode());
  annotateConditionalLinks();
  bindToggleButtons();
})();
