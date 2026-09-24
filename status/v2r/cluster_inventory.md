# V2R cluster inventory

2026-09-24T09:18:23.218316+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 324466638848 available bytes; 81.90% used; 112489962 free inodes.

server1 `/home`: 324466638848 available bytes; 81.90% used; 112489962 free inodes.

server1 `/tmp`: 324466638848 available bytes; 81.90% used; 112489962 free inodes.

server1 `/var/tmp`: 324466638848 available bytes; 81.90% used; 112489962 free inodes.

server1 `/mnt/raid5`: 503204409344 available bytes; 97.69% used; 337714752 free inodes.
| server2 | True | [] | [] |

server2 `/`: 57777602560 available bytes; 96.78% used; 110430850 free inodes.

server2 `/home`: 57777602560 available bytes; 96.78% used; 110430850 free inodes.

server2 `/tmp`: 57777602560 available bytes; 96.78% used; 110430850 free inodes.

server2 `/var/tmp`: 57777602560 available bytes; 96.78% used; 110430850 free inodes.

server2 `/mnt/raid5`: 514970955776 available bytes; 96.44% used; 445178170 free inodes.
| server3 | True | [] | [] |

server3 `/`: 85881057280 available bytes; 95.21% used; 114199165 free inodes.

server3 `/home`: 85881057280 available bytes; 95.21% used; 114199165 free inodes.

server3 `/data`: 165883621376 available bytes; 97.71% used; 225821129 free inodes.

server3 `/tmp`: 85881057280 available bytes; 95.21% used; 114199165 free inodes.

server3 `/var/tmp`: 85881057280 available bytes; 95.21% used; 114199165 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105758199808 available bytes; 94.10% used; 114349053 free inodes.

server4 `/home`: 105758199808 available bytes; 94.10% used; 114349053 free inodes.

server4 `/data`: 302824325120 available bytes; 95.81% used; 225273342 free inodes.

server4 `/tmp`: 105758199808 available bytes; 94.10% used; 114349053 free inodes.

server4 `/var/tmp`: 105758199808 available bytes; 94.10% used; 114349053 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
