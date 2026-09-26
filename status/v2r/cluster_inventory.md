# V2R cluster inventory

2026-09-26T05:49:43.852362+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318781378560 available bytes; 82.22% used; 112476281 free inodes.

server1 `/home`: 318781378560 available bytes; 82.22% used; 112476281 free inodes.

server1 `/tmp`: 318781378560 available bytes; 82.22% used; 112476281 free inodes.

server1 `/var/tmp`: 318781378560 available bytes; 82.22% used; 112476281 free inodes.

server1 `/mnt/raid5`: 237006151680 available bytes; 98.91% used; 337540029 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22745554944 available bytes; 98.73% used; 110405661 free inodes.

server2 `/home`: 22745554944 available bytes; 98.73% used; 110405661 free inodes.

server2 `/tmp`: 22745554944 available bytes; 98.73% used; 110405661 free inodes.

server2 `/var/tmp`: 22745554944 available bytes; 98.73% used; 110405661 free inodes.

server2 `/mnt/raid5`: 274966667264 available bytes; 98.10% used; 445034175 free inodes.
| server3 | True | [] | [] |

server3 `/`: 83186642944 available bytes; 95.36% used; 114148039 free inodes.

server3 `/home`: 83186642944 available bytes; 95.36% used; 114148039 free inodes.

server3 `/data`: 124237529088 available bytes; 98.28% used; 225823909 free inodes.

server3 `/tmp`: 83186642944 available bytes; 95.36% used; 114148039 free inodes.

server3 `/var/tmp`: 83186642944 available bytes; 95.36% used; 114148039 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106094379008 available bytes; 94.08% used; 114348210 free inodes.

server4 `/home`: 106094379008 available bytes; 94.08% used; 114348210 free inodes.

server4 `/data`: 106989084672 available bytes; 98.52% used; 224929128 free inodes.

server4 `/tmp`: 106094379008 available bytes; 94.08% used; 114348210 free inodes.

server4 `/var/tmp`: 106094379008 available bytes; 94.08% used; 114348210 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
