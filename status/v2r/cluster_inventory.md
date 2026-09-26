# V2R cluster inventory

2026-09-26T04:11:04.299404+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318419689472 available bytes; 82.24% used; 112476275 free inodes.

server1 `/home`: 318419689472 available bytes; 82.24% used; 112476275 free inodes.

server1 `/tmp`: 318419689472 available bytes; 82.24% used; 112476275 free inodes.

server1 `/var/tmp`: 318419689472 available bytes; 82.24% used; 112476275 free inodes.

server1 `/mnt/raid5`: 330560114688 available bytes; 98.48% used; 337545556 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22936653824 available bytes; 98.72% used; 110406202 free inodes.

server2 `/home`: 22936653824 available bytes; 98.72% used; 110406202 free inodes.

server2 `/tmp`: 22936653824 available bytes; 98.72% used; 110406202 free inodes.

server2 `/var/tmp`: 22936653824 available bytes; 98.72% used; 110406202 free inodes.

server2 `/mnt/raid5`: 286035742720 available bytes; 98.02% used; 445051025 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84141219840 available bytes; 95.30% used; 114148306 free inodes.

server3 `/home`: 84141219840 available bytes; 95.30% used; 114148306 free inodes.

server3 `/data`: 124588924928 available bytes; 98.28% used; 225819841 free inodes.

server3 `/tmp`: 84141219840 available bytes; 95.30% used; 114148306 free inodes.

server3 `/var/tmp`: 84141219840 available bytes; 95.30% used; 114148306 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 106002989056 available bytes; 94.08% used; 114348208 free inodes.

server4 `/home`: 106002989056 available bytes; 94.08% used; 114348208 free inodes.

server4 `/data`: 109671329792 available bytes; 98.48% used; 224929429 free inodes.

server4 `/tmp`: 106002989056 available bytes; 94.08% used; 114348208 free inodes.

server4 `/var/tmp`: 106002989056 available bytes; 94.08% used; 114348208 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
