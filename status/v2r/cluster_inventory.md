# V2R cluster inventory

2026-09-26T03:45:52.769500+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318417633280 available bytes; 82.24% used; 112476273 free inodes.

server1 `/home`: 318417633280 available bytes; 82.24% used; 112476273 free inodes.

server1 `/tmp`: 318417633280 available bytes; 82.24% used; 112476273 free inodes.

server1 `/var/tmp`: 318417633280 available bytes; 82.24% used; 112476273 free inodes.

server1 `/mnt/raid5`: 330988339200 available bytes; 98.48% used; 337545734 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22939951104 available bytes; 98.72% used; 110406218 free inodes.

server2 `/home`: 22939951104 available bytes; 98.72% used; 110406218 free inodes.

server2 `/tmp`: 22939951104 available bytes; 98.72% used; 110406218 free inodes.

server2 `/var/tmp`: 22939951104 available bytes; 98.72% used; 110406218 free inodes.

server2 `/mnt/raid5`: 286785732608 available bytes; 98.02% used; 445052056 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84313325568 available bytes; 95.30% used; 114152364 free inodes.

server3 `/home`: 84313325568 available bytes; 95.30% used; 114152364 free inodes.

server3 `/data`: 125357309952 available bytes; 98.27% used; 225830316 free inodes.

server3 `/tmp`: 84313325568 available bytes; 95.30% used; 114152364 free inodes.

server3 `/var/tmp`: 84313325568 available bytes; 95.30% used; 114152364 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105766219776 available bytes; 94.10% used; 114346784 free inodes.

server4 `/home`: 105766219776 available bytes; 94.10% used; 114346784 free inodes.

server4 `/data`: 108867403776 available bytes; 98.50% used; 224914705 free inodes.

server4 `/tmp`: 105766219776 available bytes; 94.10% used; 114346784 free inodes.

server4 `/var/tmp`: 105766219776 available bytes; 94.10% used; 114346784 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
