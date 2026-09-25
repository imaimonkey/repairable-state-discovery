# V2R cluster inventory

2026-09-25T16:45:26.799215+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318682980352 available bytes; 82.22% used; 112476339 free inodes.

server1 `/home`: 318682980352 available bytes; 82.22% used; 112476339 free inodes.

server1 `/tmp`: 318682980352 available bytes; 82.22% used; 112476339 free inodes.

server1 `/var/tmp`: 318682980352 available bytes; 82.22% used; 112476339 free inodes.

server1 `/mnt/raid5`: 363869265920 available bytes; 98.33% used; 337544242 free inodes.
| server2 | True | ['2', '3', '4', '5', '6'] | [] | reference_compatible=False |

server2 `/`: 23108788224 available bytes; 98.71% used; 110407940 free inodes.

server2 `/home`: 23108788224 available bytes; 98.71% used; 110407940 free inodes.

server2 `/tmp`: 23108788224 available bytes; 98.71% used; 110407940 free inodes.

server2 `/var/tmp`: 23108788224 available bytes; 98.71% used; 110407940 free inodes.

server2 `/mnt/raid5`: 317371932672 available bytes; 97.81% used; 445069975 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84397010944 available bytes; 95.29% used; 114152641 free inodes.

server3 `/home`: 84397010944 available bytes; 95.29% used; 114152641 free inodes.

server3 `/data`: 133786247168 available bytes; 98.15% used; 225805455 free inodes.

server3 `/tmp`: 84397010944 available bytes; 95.29% used; 114152641 free inodes.

server3 `/var/tmp`: 84397010944 available bytes; 95.29% used; 114152641 free inodes.
| server4 | True | ['5'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105635676160 available bytes; 94.11% used; 114349642 free inodes.

server4 `/home`: 105635676160 available bytes; 94.11% used; 114349642 free inodes.

server4 `/data`: 229999169536 available bytes; 96.82% used; 224933684 free inodes.

server4 `/tmp`: 105635676160 available bytes; 94.11% used; 114349642 free inodes.

server4 `/var/tmp`: 105635676160 available bytes; 94.11% used; 114349642 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
