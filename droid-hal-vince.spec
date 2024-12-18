# These and other macros are documented in dhd/droid-hal-device.inc
%define device vince
%define vendor xiaomi
%define vendor_pretty Xiaomi
%define device_pretty Redmi 5 Plus
%define installable_zip 1
%define droid_target_aarch64 1
%define android_version_major 7

# Entries migrated from the old rpm/droid-hal-hammerhead.spec
%define enable_kernel_update 1

%define makefstab_skip_entries /dev/cpuctl /dev/bfqio /dev/stune /oem

%define straggler_files \
/init.qcom.sh \
/init.qcom.usb.sh \
/bugreports \
/d \
/cache \
/file_contexts.bin \
/property_contexts \
/seapp_contexts \
/sdcard \
/selinux_version \
/service_contexts \
/vendor \
/charger \
/sepolicy \
/usr/libexec/droid-hybris/system/etc/init/hybris_extras.rc \
/usr/libexec/droid-hybris/system/etc/init/servicemanager.rc \
%{nil}

 
%define android_config \
#define WANT_ADRENO_QUIRKS 1\
%{nil}

%include rpm/dhd/droid-hal-device.inc
