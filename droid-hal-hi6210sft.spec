#These and other macros are documented in dhd/droid-hal-device.inc
%define device hi6210sft
%define vendor huawei
%define vendor_pretty Huawei
%define device_pretty P8Lite
%define installable_zip 1
%define enable_kernel_update 1

%define straggler_files\
    /selinux_version\
    /service_contexts\
%{nil}
%include rpm/dhd/droid-hal-device.inc
