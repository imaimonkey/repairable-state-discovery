# V2R cluster inventory

2026-09-24T18:57:01.706879+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 323996528640 available bytes; 81.93% used; 112481458 free inodes.

server1 `/home`: 323996528640 available bytes; 81.93% used; 112481458 free inodes.

server1 `/tmp`: 323996528640 available bytes; 81.93% used; 112481458 free inodes.

server1 `/var/tmp`: 323996528640 available bytes; 81.93% used; 112481458 free inodes.

server1 `/mnt/raid5`: 416259678208 available bytes; 98.09% used; 337636243 free inodes.
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 54470062080 available bytes; 96.96% used; 110411940 free inodes.

server2 `/home`: 54470062080 available bytes; 96.96% used; 110411940 free inodes.

server2 `/tmp`: 54470062080 available bytes; 96.96% used; 110411940 free inodes.

server2 `/var/tmp`: 54470062080 available bytes; 96.96% used; 110411940 free inodes.

server2 `/mnt/raid5`: 495916204032 available bytes; 96.57% used; 445160060 free inodes.
| server3 | True | ['1', '3'] | [] | reference_compatible=True |

server3 `/`: 84407308288 available bytes; 95.29% used; 114156157 free inodes.

server3 `/home`: 84407308288 available bytes; 95.29% used; 114156157 free inodes.

server3 `/data`: 152573353984 available bytes; 97.89% used; 225800061 free inodes.

server3 `/tmp`: 84407308288 available bytes; 95.29% used; 114156157 free inodes.

server3 `/var/tmp`: 84407308288 available bytes; 95.29% used; 114156157 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105661132800 available bytes; 94.10% used; 114348479 free inodes.

server4 `/home`: 105661132800 available bytes; 94.10% used; 114348479 free inodes.

server4 `/data`: 89945899008 available bytes; 98.76% used; 225267470 free inodes.

server4 `/tmp`: 105661132800 available bytes; 94.10% used; 114348479 free inodes.

server4 `/var/tmp`: 105661132800 available bytes; 94.10% used; 114348479 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
