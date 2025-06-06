from functools import partial
from insights.core.context import SosArchiveContext
from insights.core.spec_factory import simple_file, first_of, first_file, glob_file, head
from insights.specs import Specs

first_file = partial(first_file, context=SosArchiveContext)
glob_file = partial(glob_file, context=SosArchiveContext)
simple_file = partial(simple_file, context=SosArchiveContext)


class SosSpecs(Specs):
    alternatives_display_python = simple_file("sos_commands/alternatives/alternatives_--display_python")
    api_server_log = glob_file("/var/log/pods/openshift-kube-apiserver*/*/*.log")
    auditctl_rules = simple_file("sos_commands/auditd/auditctl_-l")
    auditctl_status = simple_file("sos_commands/auditd/auditctl_-s")
    auditd_conf = simple_file("/etc/audit/auditd.conf")
    audispd_conf = simple_file("/etc/audisp/audispd.conf")
    autofs_conf = simple_file("/etc/autofs.conf")
    blkid = first_file(["sos_commands/block/blkid_-c_.dev.null", "sos_commands/filesys/blkid_-c_.dev.null"])
    buddyinfo = simple_file("proc/buddyinfo")
    candlepin_error_log = first_of([
        simple_file("var/log/candlepin/error.log"),
        simple_file(r"sos_commands/foreman/foreman-debug/var/log/candlepin/error.log")
    ])
    candlepin_log = first_of([
        simple_file("/var/log/candlepin/candlepin.log"),
        simple_file("sos_commands/foreman/foreman-debug/var/log/candlepin/candlepin.log")
    ])
    catalina_out = glob_file("var/log/tomcat*/catalina.out")
    catalina_server_log = glob_file("var/log/tomcat*/catalina*.log")
    ceilometer_central_log = simple_file("/var/log/ceilometer/central.log")
    ceph_health_detail = simple_file("sos_commands/ceph/ceph_health_detail_--format_json-pretty")
    ceph_insights = simple_file("sos_commands/ceph/ceph_insights")
    ceph_log = glob_file(r"var/log/ceph/ceph.log*")
    ceph_osd_tree_text = simple_file("sos_commands/ceph/ceph_osd_tree")
    ceph_report = simple_file("sos_commands/ceph/ceph_report")
    ceph_v = simple_file("sos_commands/ceph/ceph_-v")
    checkin_conf = simple_file("/etc/splice/checkin.conf")
    chkconfig = first_file(["sos_commands/startup/chkconfig_--list", "sos_commands/services/chkconfig_--list"])
    chronyc_sources = simple_file("sos_commands/chrony/chronyc_-n_sources")
    cib_xml = first_of(
        [
            simple_file("/var/lib/pacemaker/cib/cib.xml"),
            head(
                glob_file("sos_commands/pacemaker/crm_report/*/cib.xml")
            )
        ]
    )
    cinder_volume_log = first_file(["/var/log/containers/cinder/volume.log", "/var/log/containers/cinder/cinder-volume.log", "/var/log/cinder/volume.log"])
    cloud_cfg_filtered = simple_file('/etc/cloud/cloud.cfg')
    cni_podman_bridge_conf = simple_file("/etc/cni/net.d/87-podman-bridge.conflist")
    cobbler_modules_conf = first_file(["/etc/cobbler/modules.conf", "/conf/cobbler/modules.conf"])
    cobbler_settings = first_file(["/etc/cobbler/settings", "/conf/cobbler/settings"])
    containers_policy = simple_file("/etc/containers/policy.json")
    controller_manager_log = glob_file("/var/log/pods/openshift-kube-controller-manager*/*/*.log")
    corosync_cmapctl = glob_file("sos_commands/corosync/corosync-cmapctl*")
    cpe = simple_file("/etc/system-release-cpe")
    cpu_smt_control = simple_file("sys/devices/system/cpu/smt/control")
    cpupower_frequency_info = simple_file("sos_commands/processor/cpupower_frequency-info")
    crictl_logs = glob_file(["sos_commands/crio/containers/crictl_logs_-t*", "sos_commands/crio/containers/logs/crictl_logs_-t*"])
    crio_conf = glob_file([r"etc/crio/crio.conf", r"etc/crio/crio.conf.d/*"])
    cups_files_conf = simple_file("/etc/cups/cups-files.conf")
    cups_ppd = glob_file("etc/cups/ppd/*")
    cupsd_conf = simple_file("/etc/cups/cupsd.conf")
    date = first_of([simple_file("sos_commands/general/date"), simple_file("sos_commands/date/date")])
    df__al = first_file(["sos_commands/filesys/df_-al", "sos_commands/filesys/df_-al_-x_autofs"])
    dirsrv = simple_file("/etc/sysconfig/dirsrv")
    dirsrv_access = glob_file("var/log/dirsrv/*/access*")
    display_java = simple_file("sos_commands/java/alternatives_--display_java")
    dm_mod_use_blk_mq = simple_file("/sys/module/dm_mod/parameters/use_blk_mq")
    dmesg = first_file(["sos_commands/kernel/dmesg", "sos_commands/general/dmesg", "var/log/dmesg"])
    dmidecode = simple_file("sos_commands/hardware/dmidecode")
    dmsetup_info = simple_file("sos_commands/devicemapper/dmsetup_info_-c")
    dmsetup_status = simple_file("sos_commands/devicemapper/dmsetup_status")
    dnf_modules = glob_file("/etc/dnf/modules.d/*.module")
    dnf_module_list = simple_file("/sos_commands/dnf/dnf_module_list")
    dnsmasq_config = glob_file(["/etc/dnsmasq.conf", "/etc/dnsmasq.d/*.conf"])
    docker_host_machine_id = simple_file("/etc/redhat-access-insights/machine-id")
    docker_info = simple_file("sos_commands/docker/docker_info")
    docker_list_containers = first_file(["sos_commands/docker/docker_ps_-a", "sos_commands/docker/docker_ps"])
    docker_list_images = simple_file("sos_commands/docker/docker_images")
    docker_storage = simple_file("/etc/sysconfig/docker-storage")
    dumpe2fs_h = glob_file("sos_commands/filesys/dumpe2fs_-h_*")
    eap_json_reports = glob_file(r"/var/tmp/insights-runtimes/uploads/*.json")
    ethtool = glob_file("sos_commands/networking/ethtool_*", ignore="ethtool_-.*")
    ethtool_S = glob_file("sos_commands/networking/ethtool_-S_*")
    ethtool_T = glob_file("sos_commands/networking/ethtool_-T_*")
    ethtool_a = glob_file("sos_commands/networking/ethtool_-a_*")
    ethtool_c = glob_file("sos_commands/networking/ethtool_-c_*")
    ethtool_g = glob_file("sos_commands/networking/ethtool_-g_*")
    ethtool_i = glob_file("sos_commands/networking/ethtool_-i_*")
    ethtool_k = glob_file("sos_commands/networking/ethtool_-k_*")
    firewall_cmd_list_all_zones = simple_file("sos_commands/firewalld/firewall-cmd_--list-all-zones")
    foreman_production_log = first_of([simple_file("/var/log/foreman/production.log"), simple_file("sos_commands/foreman/foreman-debug/var/log/foreman/production.log")])
    foreman_proxy_conf = first_of([simple_file("/etc/foreman-proxy/settings.yml"), simple_file("sos_commands/foreman/foreman-debug/etc/foreman-proxy/settings.yml")])
    foreman_proxy_log = first_of([simple_file("/var/log/foreman-proxy/proxy.log"), simple_file("sos_commands/foreman/foreman-debug/var/log/foreman-proxy/proxy.log")])
    foreman_satellite_log = first_of([simple_file("/var/log/foreman-installer/satellite.log"), simple_file("sos_commands/foreman/foreman-debug/var/log/foreman-installer/satellite.log")])
    foreman_ssl_access_ssl_log = first_file(["var/log/httpd/foreman-ssl_access_ssl.log", r"sos_commands/foreman/foreman-debug/var/log/httpd/foreman-ssl_access_ssl.log"])
    foreman_tasks_config = first_file(["/etc/sysconfig/foreman-tasks", "/etc/sysconfig/dynflowd"])
    freeipa_healthcheck_log = simple_file("/var/log/ipa/healthcheck/healthcheck.log")
    getcert_list = first_file(["sos_commands/ipa/ipa-getcert_list", "sos_commands/ipa/getcert_list"])
    glance_api_log = first_file(["/var/log/containers/glance/api.log", "/var/log/glance/api.log"])
    gluster_peer_status = simple_file("sos_commands/gluster/gluster_peer_status")
    gluster_v_info = simple_file("sos_commands/gluster/gluster_volume_info")
    gluster_v_status = simple_file("sos_commands/gluster/gluster_volume_status")
    gnocchi_conf = first_file(["/var/lib/config-data/puppet-generated/gnocchi/etc/gnocchi/gnocchi.conf", "/etc/gnocchi/gnocchi.conf"])
    gnocchi_metricd_log = first_file(["/var/log/containers/gnocchi/gnocchi-metricd.log", "/var/log/gnocchi/metricd.log"])
    grubenv = first_file(["/boot/grub2/grubenv", "/boot/efi/EFI/redhat/grubenv"])
    hammer_ping = first_file(["sos_commands/foreman/hammer_ping", "sos_commands/foreman/foreman-debug/hammer-ping"])
    heat_engine_log = first_file(["/var/log/containers/heat/heat-engine.log", "/var/log/heat/heat-engine.log"])
    hostname = first_file(["sos_commands/general/hostname_-f", "sos_commands/host/hostname_-f"])
    hostname_default = first_file(["sos_commands/general/hostname", "sos_commands/host/hostname", "/etc/hostname", "hostname"])
    hostname_short = first_file(["sos_commands/general/hostname", "sos_commands/host/hostname", "/etc/hostname", "hostname"])
    httpd_M = simple_file("sos_commands/apache/apachectl_-M")
    httpd_access_log = simple_file("/var/log/httpd/access_log")
    httpd_ssl_access_log = simple_file("/var/log/httpd/ssl_access_log")
    httpd_ssl_error_log = simple_file("/var/log/httpd/ssl_error_log")
    initscript = glob_file(r"etc/rc.d/init.d/*")
    installed_rpms = first_file(["sos_commands/rpm/package-data", "installed-rpms"])
    ip6tables_permanent = simple_file("etc/sysconfig/ip6tables")
    ip_addr = first_of([simple_file("sos_commands/networking/ip_-d_address"), simple_file("sos_commands/networking/ip_address")])
    ip_neigh_show = first_file(["sos_commands/networking/ip_-s_-s_neigh_show", "sos_commands/networking/ip_neigh_show"])
    ip_route_show_table_all = simple_file("sos_commands/networking/ip_route_show_table_all")
    ip_s_link = first_of([simple_file("sos_commands/networking/ip_-s_-d_link"), simple_file("sos_commands/networking/ip_-s_link"), simple_file("sos_commands/networking/ip_link")])
    ipa_default_conf = simple_file("/etc/ipa/default.conf")
    iptables = first_file(["/etc/sysconfig/iptables", "/etc/sysconfig/iptables.save"])
    ironic_conf = first_file(["/var/lib/config-data/puppet-generated/ironic/etc/ironic/ironic.conf", "/etc/ironic/ironic.conf"])
    ironic_inspector_log = first_file(["/var/log/containers/ironic-inspector/ironic-inspector.log", "/var/log/ironic-inspector/ironic-inspector.log"])
    journal_all = simple_file("sos_commands/logs/journalctl_--no-pager")
    journal_since_boot = first_file(["sos_commands/logs/journalctl_--no-pager_--boot", "sos_commands/logs/journalctl_--no-pager_--catalog_--boot", "sos_commands/logs/journalctl_--all_--this-boot_--no-pager"])
    kerberos_kdc_log = simple_file("var/log/krb5kdc.log")
    kexec_crash_loaded = simple_file("/sys/kernel/kexec_crash_loaded")
    keystone_conf = first_file(["/var/lib/config-data/puppet-generated/keystone/etc/keystone/keystone.conf", "/etc/keystone/keystone.conf"])
    keystone_crontab = simple_file("/var/spool/cron/keystone")
    keystone_log = first_file(["/var/log/containers/keystone/keystone.log", "/var/log/keystone/keystone.log"])
    kubelet_conf = simple_file("/etc/kubernetes/kubelet.conf")
    libvirtd_qemu_log = glob_file(r"/var/log/libvirt/qemu/*.log")
    locale = simple_file("sos_commands/i18n/locale")
    ls_boot = first_file(["sos_commands/boot/ls_-lanR_.boot", "sos_commands/boot/ls_-alZR_.boot"])
    ls_dev = first_file(["sos_commands/block/ls_-lanR_.dev", "sos_commands/devicemapper/ls_-lanR_.dev", "sos_commands/block/ls_-alZR_.dev", "sos_commands/devicemapper/ls_-alZR_.dev"])
    ls_sys_firmware = first_file(["sos_commands/boot/ls_-lanR_.sys.firmware", "sos_commands/boot/ls_-alZR_.sys.firmware"])
    lsblk = first_file(["sos_commands/block/lsblk", "sos_commands/filesys/lsblk"])
    lsblk_pairs = simple_file("sos_commands/block/lsblk_-O_-P")
    lscpu = simple_file("sos_commands/processor/lscpu")
    lsinitrd = simple_file("sos_commands/boot/lsinitrd")
    lsmod = simple_file("sos_commands/kernel/lsmod")
    lsof = first_file([
        "sos_commands/process/lsof_M_-n_-l_-c",
        "sos_commands/process/lsof_-b_M_-n_-l_-c",
        "sos_commands/process/lsof_-b_M_-n_-l"
    ])
    lspci = first_of([
        simple_file("sos_commands/pci/lspci_-nnvv"),
        simple_file("sos_commands/pci/lspci_-nvv"),
        simple_file("sos_commands/pci/lspci")
    ])
    lsscsi = simple_file("sos_commands/scsi/lsscsi")
    lvm_conf = simple_file("/etc/lvm/lvm.conf")
    lvs_headings = first_file([
        "sos_commands/lvm2/lvs_-a_-o_lv_tags_devices_lv_kernel_read_ahead_lv_read_ahead_stripes_stripesize_--config_global_metadata_read_only_1_--nolocking_--foreign",
        "sos_commands/lvm2/lvs_-a_-o_lv_tags_devices_lv_kernel_read_ahead_lv_read_ahead_stripes_stripesize_--config_global_locking_type_0_metadata_read_only_1",
        "sos_commands/lvm2/lvs_-a_-o_lv_tags_devices_--config_global_locking_type_0",
        "sos_commands/lvm2/lvs_-a_-o_devices",
        "sos_commands/devicemapper/lvs_-a_-o__devices"
    ])
    manila_conf = first_file(["/var/lib/config-data/puppet-generated/manila/etc/manila/manila.conf", "/etc/manila/manila.conf"])
    mdadm_D = simple_file("sos_commands/md/mdadm_-D_.dev.md")
    mdadm_E = glob_file("sos_commands/md/mdadm_-E_*")
    mistral_executor_log = simple_file("/var/log/mistral/executor.log")
    mlx4_port = glob_file("/sys/bus/pci/devices/*/mlx4_port[0-9]")
    modinfo_filtered_modules = simple_file("sos_commands/kernel/modinfo_ALL_MODULES")
    mokutil_sbstate = simple_file("sos_commands/boot/mokutil_--sb-state")
    mongod_conf = glob_file([
        "/etc/mongod.conf",
        "/etc/opt/rh/rh-mongodb34/mongod.conf"
    ])
    mount = simple_file("sos_commands/filesys/mount_-l")
    mountinfo = simple_file("proc/self/mountinfo")
    mounts = simple_file("/proc/mounts")
    multipath__v4__ll = first_file(["sos_commands/multipath/multipath_-v4_-ll", "sos_commands/devicemapper/multipath_-v4_-ll"])
    netconsole = simple_file("/etc/sysconfig/netconsole")
    netstat = first_file(["sos_commands/networking/netstat_-neopa", "sos_commands/networking/netstat_-W_-neopa", "sos_commands/networking/netstat_-T_-neopa"])
    netstat_agn = first_of([simple_file("sos_commands/networking/netstat_-agn"), simple_file("sos_commands/networking/netstat_-W_-agn"), simple_file("sos_commands/networking/netstat_-T_-agn")])
    netstat_s = simple_file("sos_commands/networking/netstat_-s")
    neutron_conf = first_file(["/var/lib/config-data/puppet-generated/neutron/etc/neutron/neutron.conf", "/etc/neutron/neutron.conf"])
    neutron_dhcp_agent_ini = first_file(["/var/lib/config-data/puppet-generated/neutron/etc/neutron/dhcp_agent.ini", "/etc/neutron/dhcp_agent.ini"])
    neutron_l3_agent_ini = first_file(["/var/lib/config-data/puppet-generated/neutron/etc/neutron/l3_agent.ini", "/etc/neutron/l3_agent.ini"])
    neutron_l3_agent_log = first_file(["/var/log/containers/neutron/l3-agent.log", "/var/log/neutron/l3-agent.log"])
    neutron_ml2_conf = first_file(["/var/lib/config-data/puppet-generated/neutron/etc/neutron/plugins/ml2/ml2_conf.ini", "/etc/neutron/plugins/ml2/ml2_conf.ini"])
    neutron_ovs_agent_log = first_file(["/var/log/containers/neutron/openvswitch-agent.log", "/var/log/neutron/openvswitch-agent.log"])
    neutron_plugin_ini = first_file(["/var/lib/config-data/puppet-generated/neutron/etc/neutron/plugin.ini", "/etc/neutron/plugin.ini"])
    neutron_server_log = first_file(["/var/log/containers/neutron/server.log", "/var/log/neutron/server.log"])
    nmcli_dev_show = simple_file("sos_commands/networking/nmcli_device_show")
    nmcli_dev_show_sos = glob_file(["sos_commands/networking/nmcli_dev_show_*", "sos_commands/networkmanager/nmcli_dev_show_*"])
    nova_api_log = first_file(["/var/log/containers/nova/nova-api.log", "/var/log/nova/nova-api.log"])
    ntptime = simple_file("sos_commands/ntp/ntptime")
    octavia_conf = simple_file("/var/lib/config-data/puppet-generated/octavia/etc/octavia/octavia.conf")
    openvswitch_daemon_log = first_file([
        '/var/log/openvswitch/ovs-vswitchd.log',
        '/host/var/log/openvswitch/ovs-vswitchd.log'
    ])
    openvswitch_other_config = simple_file("sos_commands/openvswitch/ovs-vsctl_-t_5_get_Open_vSwitch_._other_config")
    openvswitch_server_log = simple_file('/var/log/openvswitch/ovsdb-server.log')
    osa_dispatcher_log = first_file([
        "/var/log/rhn/osa-dispatcher.log",
        "/rhn-logs/rhn/osa-dispatcher.log"
    ])
    ovirt_engine_boot_log = simple_file("/var/log/ovirt-engine/boot.log")
    ovirt_engine_confd = glob_file("/etc/ovirt-engine/engine.conf.d/*")
    ovirt_engine_console_log = simple_file("/var/log/ovirt-engine/console.log")
    ovs_vsctl_show = simple_file("sos_commands/openvswitch/ovs-vsctl_-t_5_show")
    pam_conf = simple_file("/etc/pam.conf")
    partitions = simple_file("/proc/partitions")
    pcp_openmetrics_log = simple_file("/var/log/pcp/pmcd/openmetrics.log")
    pcs_config = simple_file("sos_commands/pacemaker/pcs_config")
    pcs_quorum_status = simple_file("sos_commands/pacemaker/pcs_quorum_status")
    pcs_status = first_file(["sos_commands/pacemaker/pcs_status", "/sos_commands/pacemaker/pcs_status_--full"])
    podman_list_containers = first_file(["sos_commands/podman/podman_ps_-a", "sos_commands/podman/podman_ps"])
    podman_list_images = simple_file("sos_commands/podman/podman_images")
    postgresql_conf = first_file([
        "/var/opt/rh/rh-postgresql12/lib/pgsql/data/postgresql.conf",
        "/var/lib/pgsql/data/postgresql.conf",
        "database/postgresql.conf"
    ])
    postgresql_log = first_of(
        [
            glob_file("/var/opt/rh/rh-postgresql12/lib/pgsql/data/log/postgresql-*.log"),
            glob_file("/var/lib/pgsql/data/pg_log/postgresql-*.log"),
            glob_file("/database/postgresql-*.log")
        ]
    )
    ps_alxwww = simple_file("sos_commands/process/ps_alxwww")
    ps_aux = first_file(["sos_commands/process/ps_aux", "sos_commands/process/ps_auxwww", "sos_commands/process/ps_auxcww"])
    ps_auxcww = first_file(["sos_commands/process/ps_auxcww", "sos_commands/process/ps_auxwww", "sos_commands/process/ps_aux", "sos_commands/process/ps_auxwwwm"])
    ps_auxww = first_file(["sos_commands/process/ps_auxww", "sos_commands/process/ps_auxwww", "sos_commands/process/ps_aux", "sos_commands/process/ps_auxwwwm", "sos_commands/process/ps_auxcww"])
    pulp_worker_defaults = simple_file("etc/default/pulp_workers")
    puppet_ssl_cert_ca_pem = first_file([
        "/etc/puppetlabs/puppet/ssl/certs/ca.pem",
        "sos_commands/foreman/foreman-debug/var/lib/puppet/ssl/certs/ca.pem"
    ])
    pvs_headings = first_file([
        "sos_commands/lvm2/pvs_-a_-v_-o_pv_mda_free_pv_mda_size_pv_mda_count_pv_mda_used_count_pe_start_--config_global_metadata_read_only_1_--nolocking_--foreign",
        "sos_commands/lvm2/pvs_-a_-v_-o_pv_mda_free_pv_mda_size_pv_mda_count_pv_mda_used_count_pe_start_--config_global_locking_type_0_metadata_read_only_1",
        "sos_commands/lvm2/pvs_-a_-v_-o_pv_mda_free_pv_mda_size_pv_mda_count_pv_mda_used_count_pe_start_--config_global_locking_type_0",
        "sos_commands/lvm2/pvs_-a_-v",
        "sos_commands/devicemapper/pvs_-a_-v"
    ])
    qpid_stat_q = first_file([
        "sos_commands/pulp/qpid-stat_-q_--ssl-certificate_.etc.pki.pulp.qpid.client.crt_-b_amqps_..localhost_5671",
        "sos_commands/pulp/qpid-stat_-q_--ssl-certificate_.etc.pki.katello.qpid_client_striped.crt_-b_amqps_..localhost_5671",
        "sos_commands/katello/qpid-stat_-q_--ssl-certificate_.etc.pki.pulp.qpid.client.crt_-b_amqps_..localhost_5671",
        "sos_commands/katello/qpid-stat_-q_--ssl-certificate_.etc.pki.katello.qpid_client_striped.crt_-b_amqps_..localhost_5671",
        "sos_commands/foreman/foreman-debug/qpid-stat-q",
        "qpid-stat-q",
        "sos_commands/foreman/foreman-debug/qpid_stat_queues",
        "qpid_stat_queues"
    ])
    qpid_stat_u = first_file([
        "sos_commands/pulp/qpid-stat_-u_--ssl-certificate_.etc.pki.pulp.qpid.client.crt_-b_amqps_..localhost_5671",
        "sos_commands/pulp/qpid-stat_-u_--ssl-certificate_.etc.pki.katello.qpid_client_striped.crt_-b_amqps_..localhost_5671",
        "sos_commands/katello/qpid-stat_-u_--ssl-certificate_.etc.pki.pulp.qpid.client.crt_-b_amqps_..localhost_5671",
        "sos_commands/katello/qpid-stat_-u_--ssl-certificate_.etc.pki.katello.qpid_client_striped.crt_-b_amqps_..localhost_5671",
        "sos_commands/foreman/foreman-debug/qpid-stat-u",
        "qpid-stat-u",
        "sos_commands/foreman/foreman-debug/qpid_stat_subscriptions",
        "qpid_stat_subscriptions"
    ])
    rabbitmq_env = simple_file("/etc/rabbitmq/rabbitmq-env.conf")
    rabbitmq_logs = glob_file("/var/log/rabbitmq/rabbit@*.log", ignore=".*rabbit@.*(?<!-sasl).log$")
    rabbitmq_startup_err = simple_file("/var/log/rabbitmq/startup_err")
    rabbitmq_startup_log = simple_file("/var/log/rabbitmq/startup_log")
    rc_local = simple_file("/etc/rc.d/rc.local")
    recvq_socket_buffer = simple_file("proc/sys/net/ipv4/tcp_rmem")
    rhn_charsets = first_file(["sos_commands/satellite/rhn-charsets", "sos_commands/rhn/rhn-charsets"])
    rhn_entitlement_cert_xml = first_of([glob_file("/etc/sysconfig/rhn/rhn-entitlement-cert.xml*"),
                                   glob_file("/conf/rhn/sysconfig/rhn/rhn-entitlement-cert.xml*")])
    rhn_hibernate_conf = first_file(["/usr/share/rhn/config-defaults/rhn_hibernate.conf", "/config-defaults/rhn_hibernate.conf"])
    rhn_schema_version = simple_file("sos_commands/satellite/rhn-schema-version")
    rhn_search_daemon_log = first_file([
        "/var/log/rhn/search/rhn_search_daemon.log",
        "/rhn-logs/rhn/search/rhn_search_daemon.log"
    ])
    rhn_server_satellite_log = simple_file("var/log/rhn/rhn_server_satellite.log")
    rhn_server_xmlrpc_log = first_file([
        "/var/log/rhn/rhn_server_xmlrpc.log",
        "/rhn-logs/rhn/rhn_server_xmlrpc.log"
    ])
    rhn_taskomatic_daemon_log = first_file(["/var/log/rhn/rhn_taskomatic_daemon.log",
                                            "rhn-logs/rhn/rhn_taskomatic_daemon.log"])
    rhosp_release = simple_file("/etc/rhosp-release")
    root_crontab = first_file(["sos_commands/crontab/root_crontab", "sos_commands/cron/root_crontab"])
    route = simple_file("sos_commands/networking/route_-n")
    samba_logs = glob_file("var/log/samba/log.*")
    sap_host_profile = simple_file("/usr/sap/hostctrl/exe/host_profile")
    sched_rt_runtime_us = simple_file("/proc/sys/kernel/sched_rt_runtime_us")
    scsi_mod_use_blk_mq = simple_file("/sys/module/scsi_mod/parameters/use_blk_mq")
    sendq_socket_buffer = simple_file("proc/sys/net/ipv4/tcp_wmem")
    sestatus = simple_file("sos_commands/selinux/sestatus_-b")
    ssh_foreman_config = simple_file("/usr/share/foreman/.ssh/ssh_config")
    sssd_logs = glob_file(["/var/log/sssd/*.log", "/host/var/log/sssd/*.log"])
    subscription_manager_id = simple_file("/sos_commands/subscription_manager/subscription-manager_identity")
    subscription_manager_list_consumed = first_file([
        'sos_commands/yum/subscription-manager_list_--consumed',
        'sos_commands/subscription_manager/subscription-manager_list_--consumed',
        'sos_commands/general/subscription-manager_list_--consumed']
    )
    subscription_manager_status = simple_file("sos_commands/subscription_manager/subscription-manager_status")
    subscription_manager_list_installed = first_file([
        'sos_commands/yum/subscription-manager_list_--installed',
        'sos_commands/subscription_manager/subscription-manager_list_--installed',
        'sos_commands/general/subscription-manager_list_--installed']
    )
    swift_conf = first_file(["/var/lib/config-data/puppet-generated/swift/etc/swift/swift.conf", "/etc/swift/swift.conf"])
    swift_log = first_file(["/var/log/containers/swift/swift.log", "/var/log/swift/swift.log"])
    swift_object_expirer_conf = first_file(["/var/lib/config-data/puppet-generated/swift/etc/swift/object-expirer.conf", "/etc/swift/object-expirer.conf"])
    sys_kernel_sched_features = simple_file("/sys/kernel/debug/sched_features")
    sysconfig_chronyd = simple_file("/etc/sysconfig/chronyd")
    sysconfig_httpd = simple_file("/etc/sysconfig/httpd")
    sysconfig_irqbalance = simple_file("etc/sysconfig/irqbalance")
    sysconfig_memcached = first_file(["/var/lib/config-data/puppet-generated/memcached/etc/sysconfig/memcached", "/etc/sysconfig/memcached"])
    sysconfig_mongod = glob_file(["etc/sysconfig/mongod", "etc/opt/rh/rh-mongodb26/sysconfig/mongod"])
    sysconfig_nfs = simple_file("/etc/sysconfig/nfs")
    sysctl = simple_file("sos_commands/kernel/sysctl_-a")
    systemctl_list_unit_files = simple_file("sos_commands/systemd/systemctl_list-unit-files")
    systemctl_list_units = first_file(["sos_commands/systemd/systemctl_list-units", "sos_commands/systemd/systemctl_list-units_--all"])
    systemctl_show_all_services = simple_file("sos_commands/systemd/systemctl_show_service_--all")
    systemctl_status_all = simple_file("sos_commands/systemd/systemctl_status_--all")
    systemd_analyze_blame = simple_file("sos_commands/systemd/systemd-analyze_blame")
    systemd_system_origin_accounting = simple_file("/etc/systemd/system.conf.d/origin-accounting.conf")
    teamdctl_config_dump = glob_file("sos_commands/teamd/teamdctl_*_config_dump")
    teamdctl_state_dump = glob_file("sos_commands/teamd/teamdctl_*_state_dump")
    testparm_s = simple_file("sos_commands/samba/testparm_s")
    tomcat_web_xml = first_of([glob_file("/etc/tomcat*/web.xml"),
                                  glob_file("/conf/tomcat/tomcat*/web.xml")])
    tuned_adm = simple_file("sos_commands/tuned/tuned-adm_list")
    tuned_conf = simple_file("/etc/tuned.conf")
    uname = simple_file("sos_commands/kernel/uname_-a")
    uptime = first_of([simple_file("sos_commands/general/uptime"), simple_file("sos_commands/host/uptime")])
    var_qemu_xml = glob_file(r"var/run/libvirt/qemu/*.xml")
    vdsm_conf = simple_file("etc/vdsm/vdsm.conf")
    vdsm_id = simple_file("etc/vdsm/vdsm.id")
    vdsm_import_log = glob_file("var/log/vdsm/import/import-*.log")
    vgdisplay = first_file([
        "sos_commands/lvm2/vgdisplay_-vv_--config_global_metadata_read_only_1_--nolocking_--foreign",
        "sos_commands/lvm2/vgdisplay_-vv_--config_global_locking_type_0_metadata_read_only_1",
        "sos_commands/lvm2/vgdisplay_-vv_--config_global_locking_type_0",
        "sos_commands/lvm2/vgdisplay_-vv",
        "sos_commands/devicemapper/vgdisplay_-vv"
    ])
    vgs_headings = first_file([
        "sos_commands/lvm2/vgs_-v_-o_vg_mda_count_vg_mda_free_vg_mda_size_vg_mda_used_count_vg_tags_systemid_--config_global_metadata_read_only_1_--nolocking_--foreign",
        "sos_commands/lvm2/vgs_-v_-o_vg_mda_count_vg_mda_free_vg_mda_size_vg_mda_used_count_vg_tags_--config_global_locking_type_0_metadata_read_only_1",
        "sos_commands/lvm2/vgs_-v_-o_vg_mda_count_vg_mda_free_vg_mda_size_vg_mda_used_count_vg_tags_--config_global_locking_type_0",
        "sos_commands/lvm2/vgs_-v",
        "sos_commands/devicemapper/vgs_-v"
    ])
    virsh_list_all = simple_file("sos_commands/virsh/virsh_-r_list_--all")
    virtlogd_conf = simple_file("/etc/libvirt/virtlogd.conf")
    vmcore_dmesg = glob_file("/var/crash/*/vmcore-dmesg.txt")
    vmware_tools_conf = simple_file("etc/vmware-tools/tools.conf")
    xfs_info = glob_file("sos_commands/xfs/xfs_info*")
    yum_log = simple_file("/var/log/yum.log")
    yum_repolist = simple_file("sos_commands/yum/yum_-C_repolist")
