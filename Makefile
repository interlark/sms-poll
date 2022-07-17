.PHONY: build_web_apps dev_server dev_client build_x86
		build_x86_64 build_armeabi-v7a build_arm64-v8a clean

build_x86: ARCH = x86
build_x86_64: ARCH = x86_64
build_armeabi-v7a: ARCH = armeabi-v7a
build_arm64-v8a: ARCH = arm64-v8a

dev_server:
	DEBUG=1 uvicorn --app-dir "$(CURDIR)/sms_poll/server" --port 5000 --reload main:app

dev_client:
	npm start --prefix "$(CURDIR)/sms_poll/client"

build_static:
	npm install -C "$(CURDIR)/sms_poll/client"
	for app in "poll" "admin" ; do \
		rm -rf "$(CURDIR)/sms_poll/server/app/static/$${app}"; \
		npx parcel build "$(CURDIR)/sms_poll/client/src/apps/$${app}/index.html" \
			--public-url "." \
			--dist-dir "$(CURDIR)/sms_poll/server/app/static/$${app}" \
			--no-source-maps; \
	done

--build_apk:
	p4a apk --private "$(CURDIR)/sms_poll/server" \
		--package=org.interlark.sms_poll \
		--name "SMS Poll" \
		--requirements fastapi,tortoise-orm,uvicorn,phonenumbers \
		--bootstrap=webview \
		--dist_name SMSPoll \
		--version 0.1.0 \
		--arch $(ARCH) \
		--local-recipes "$(CURDIR)/build/recipes" \
		--orientation sensor \
		--permission INTERNET \
		--permission RECEIVE_SMS \
		--permission READ_PHONE_NUMBERS \
		--permission ACCESS_WIFI_STATE \
		--icon "$(CURDIR)/build/assets/icon.png" \
		--icon-fg "$(CURDIR)/build/assets/icon_fg.png" \
		--icon-bg "$(CURDIR)/build/assets/icon_bg.png" \
		--presplash "$(CURDIR)/build/assets/presplash.jpg" \
		--asset "$(CURDIR)/build/assets/_load.html:." \
		--blacklist "$(CURDIR)/build/blacklist.txt"

build_x86 build_x86_64 build_armeabi-v7a build_arm64-v8a: build_static --build_apk

clean:
	p4a clean_all
	rm -rf *.apk
	find "$(CURDIR)" -type f -name "*.py[co]" -delete
	find "$(CURDIR)" -type d -name "__pycache__" -delete
	find "$(CURDIR)" -depth -type d -name ".mypy_cache" -exec rm -r "{}" +
	find "$(CURDIR)" -depth -type d -name ".pytest_cache" -exec rm -r "{}" +