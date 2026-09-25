# V2R cluster inventory

2026-09-25T16:56:07.784211+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318681436160 available bytes; 82.22% used; 112476339 free inodes.

server1 `/home`: 318681436160 available bytes; 82.22% used; 112476339 free inodes.

server1 `/tmp`: 318681436160 available bytes; 82.22% used; 112476339 free inodes.

server1 `/var/tmp`: 318681436160 available bytes; 82.22% used; 112476339 free inodes.

server1 `/mnt/raid5`: 364364124160 available bytes; 98.33% used; 337543958 free inodes.
| server2 | True | ['2', '3', '4', '5', '6'] | [] | reference_compatible=False |

server2 `/`: 23107596288 available bytes; 98.71% used; 110407938 free inodes.

server2 `/home`: 23107596288 available bytes; 98.71% used; 110407938 free inodes.

server2 `/tmp`: 23107596288 available bytes; 98.71% used; 110407938 free inodes.

server2 `/var/tmp`: 23107596288 available bytes; 98.71% used; 110407938 free inodes.

server2 `/mnt/raid5`: 317050466304 available bytes; 97.81% used; 445069413 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84396527616 available bytes; 95.29% used; 114152621 free inodes.

server3 `/home`: 84396527616 available bytes; 95.29% used; 114152621 free inodes.

server3 `/data`: 133780746240 available bytes; 98.15% used; 225805212 free inodes.

server3 `/tmp`: 84396527616 available bytes; 95.29% used; 114152621 free inodes.

server3 `/var/tmp`: 84396527616 available bytes; 95.29% used; 114152621 free inodes.
| server4 | True | ['5'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105635405824 available bytes; 94.11% used; 114349641 free inodes.

server4 `/home`: 105635405824 available bytes; 94.11% used; 114349641 free inodes.

server4 `/data`: 229979439104 available bytes; 96.82% used; 224933466 free inodes.

server4 `/tmp`: 105635405824 available bytes; 94.11% used; 114349641 free inodes.

server4 `/var/tmp`: 105635405824 available bytes; 94.11% used; 114349641 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
