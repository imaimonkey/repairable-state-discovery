# V2R cluster inventory

2026-09-24T09:27:42.299844+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 324458684416 available bytes; 81.90% used; 112489888 free inodes.

server1 `/home`: 324458684416 available bytes; 81.90% used; 112489888 free inodes.

server1 `/tmp`: 324458684416 available bytes; 81.90% used; 112489888 free inodes.

server1 `/var/tmp`: 324458684416 available bytes; 81.90% used; 112489888 free inodes.

server1 `/mnt/raid5`: 502507130880 available bytes; 97.69% used; 337713644 free inodes.
| server2 | True | [] | [] |

server2 `/`: 57767874560 available bytes; 96.78% used; 110430819 free inodes.

server2 `/home`: 57767874560 available bytes; 96.78% used; 110430819 free inodes.

server2 `/tmp`: 57767874560 available bytes; 96.78% used; 110430819 free inodes.

server2 `/var/tmp`: 57767874560 available bytes; 96.78% used; 110430819 free inodes.

server2 `/mnt/raid5`: 514674466816 available bytes; 96.44% used; 445177730 free inodes.
| server3 | True | [] | [] |

server3 `/`: 85493628928 available bytes; 95.23% used; 114184092 free inodes.

server3 `/home`: 85493628928 available bytes; 95.23% used; 114184092 free inodes.

server3 `/data`: 165358702592 available bytes; 97.71% used; 225820920 free inodes.

server3 `/tmp`: 85493628928 available bytes; 95.23% used; 114184092 free inodes.

server3 `/var/tmp`: 85493628928 available bytes; 95.23% used; 114184092 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105757827072 available bytes; 94.10% used; 114349047 free inodes.

server4 `/home`: 105757827072 available bytes; 94.10% used; 114349047 free inodes.

server4 `/data`: 154931265536 available bytes; 97.86% used; 225273290 free inodes.

server4 `/tmp`: 105757827072 available bytes; 94.10% used; 114349047 free inodes.

server4 `/var/tmp`: 105757827072 available bytes; 94.10% used; 114349047 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
