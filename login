#!/data/data/com.termux/files/usr/bin/sh

if [ $# = 0 ] && [ -f /data/data/com.termux/files/usr/etc/motd ] && [ ! -f ~/.hushlogin ] && [ -z "$TERMUX_HUSHLOGIN" ]; then
	bash $HOME/start-ubuntu20.sh
else
	# This variable shouldn't be kept set.
	unset TERMUX_HUSHLOGIN
fi

if [ -G ~/.termux/shell ]; then
	export SHELL="`realpath ~/.termux/shell`"
else
	for file in /data/data/com.termux/files/usr/bin/bash /data/data/com.termux/files/usr/bin/sh /system/bin/sh; do
		if [ -x $file ]; then
			export SHELL=$file
			break
		fi
	done
fi

if [ -f /data/data/com.termux/files/usr/lib/libtermux-exec.so ]; then
	export LD_PRELOAD=/data/data/com.termux/files/usr/lib/libtermux-exec.so
	$SHELL -c "coreutils --coreutils-prog=true" > /dev/null 2>&1 || unset LD_PRELOAD
fi

if [ -n "$TERM" ]; then
	exec "$SHELL" -l "$@"
else
	exec "$SHELL" "$@"
fi
