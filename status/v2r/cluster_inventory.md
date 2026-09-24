# V2R cluster inventory

2026-09-24T09:19:56.425455+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 324465405952 available bytes; 81.90% used; 112489948 free inodes.

server1 `/home`: 324465405952 available bytes; 81.90% used; 112489948 free inodes.

server1 `/tmp`: 324465405952 available bytes; 81.90% used; 112489948 free inodes.

server1 `/var/tmp`: 324465405952 available bytes; 81.90% used; 112489948 free inodes.

server1 `/mnt/raid5`: 503192248320 available bytes; 97.69% used; 337714567 free inodes.
| server2 | True | [] | [] |

server2 `/`: 57776754688 available bytes; 96.78% used; 110430844 free inodes.

server2 `/home`: 57776754688 available bytes; 96.78% used; 110430844 free inodes.

server2 `/tmp`: 57776754688 available bytes; 96.78% used; 110430844 free inodes.

server2 `/var/tmp`: 57776754688 available bytes; 96.78% used; 110430844 free inodes.

server2 `/mnt/raid5`: 514918797312 available bytes; 96.44% used; 445178097 free inodes.
| server3 | True | ['0'] | [] |

server3 `/`: 85866733568 available bytes; 95.21% used; 114199160 free inodes.

server3 `/home`: 85866733568 available bytes; 95.21% used; 114199160 free inodes.

server3 `/data`: 165879197696 available bytes; 97.71% used; 225821091 free inodes.

server3 `/tmp`: 85866733568 available bytes; 95.21% used; 114199160 free inodes.

server3 `/var/tmp`: 85866733568 available bytes; 95.21% used; 114199160 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105758138368 available bytes; 94.10% used; 114349051 free inodes.

server4 `/home`: 105758138368 available bytes; 94.10% used; 114349051 free inodes.

server4 `/data`: 288103456768 available bytes; 96.02% used; 225273320 free inodes.

server4 `/tmp`: 105758138368 available bytes; 94.10% used; 114349051 free inodes.

server4 `/var/tmp`: 105758138368 available bytes; 94.10% used; 114349051 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
