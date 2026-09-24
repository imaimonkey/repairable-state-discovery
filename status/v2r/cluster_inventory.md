# V2R cluster inventory

2026-09-24T11:05:36.047626+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 324373176320 available bytes; 81.90% used; 112488998 free inodes.

server1 `/home`: 324373176320 available bytes; 81.90% used; 112488998 free inodes.

server1 `/tmp`: 324373176320 available bytes; 81.90% used; 112488998 free inodes.

server1 `/var/tmp`: 324373176320 available bytes; 81.90% used; 112488998 free inodes.

server1 `/mnt/raid5`: 481946886144 available bytes; 97.79% used; 337692756 free inodes.
| server2 | True | ['6'] | [] |

server2 `/`: 57694687232 available bytes; 96.78% used; 110430237 free inodes.

server2 `/home`: 57694687232 available bytes; 96.78% used; 110430237 free inodes.

server2 `/tmp`: 57694687232 available bytes; 96.78% used; 110430237 free inodes.

server2 `/var/tmp`: 57694687232 available bytes; 96.78% used; 110430237 free inodes.

server2 `/mnt/raid5`: 511679254528 available bytes; 96.46% used; 445174347 free inodes.
| server3 | True | [] | [] |

server3 `/`: 85332545536 available bytes; 95.24% used; 114170710 free inodes.

server3 `/home`: 85332545536 available bytes; 95.24% used; 114170710 free inodes.

server3 `/data`: 163980271616 available bytes; 97.73% used; 225817457 free inodes.

server3 `/tmp`: 85332545536 available bytes; 95.24% used; 114170710 free inodes.

server3 `/var/tmp`: 85332545536 available bytes; 95.24% used; 114170710 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105733771264 available bytes; 94.10% used; 114348923 free inodes.

server4 `/home`: 105733771264 available bytes; 94.10% used; 114348923 free inodes.

server4 `/data`: 115739287552 available bytes; 98.40% used; 225258210 free inodes.

server4 `/tmp`: 105733771264 available bytes; 94.10% used; 114348923 free inodes.

server4 `/var/tmp`: 105733771264 available bytes; 94.10% used; 114348923 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
