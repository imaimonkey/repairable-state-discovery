# V2R cluster inventory

2026-09-25T20:17:52.560676+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318708543488 available bytes; 82.22% used; 112476339 free inodes.

server1 `/home`: 318708543488 available bytes; 82.22% used; 112476339 free inodes.

server1 `/tmp`: 318708543488 available bytes; 82.22% used; 112476339 free inodes.

server1 `/var/tmp`: 318708543488 available bytes; 82.22% used; 112476339 free inodes.

server1 `/mnt/raid5`: 369858543616 available bytes; 98.30% used; 337540534 free inodes.
| server2 | True | ['2', '3', '4', '5', '6'] | [] | reference_compatible=False |

server2 `/`: 23086747648 available bytes; 98.71% used; 110407934 free inodes.

server2 `/home`: 23086747648 available bytes; 98.71% used; 110407934 free inodes.

server2 `/tmp`: 23086747648 available bytes; 98.71% used; 110407934 free inodes.

server2 `/var/tmp`: 23086747648 available bytes; 98.71% used; 110407934 free inodes.

server2 `/mnt/raid5`: 310757867520 available bytes; 97.85% used; 445063129 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84380610560 available bytes; 95.29% used; 114152620 free inodes.

server3 `/home`: 84380610560 available bytes; 95.29% used; 114152620 free inodes.

server3 `/data`: 127187013632 available bytes; 98.24% used; 225808252 free inodes.

server3 `/tmp`: 84380610560 available bytes; 95.29% used; 114152620 free inodes.

server3 `/var/tmp`: 84380610560 available bytes; 95.29% used; 114152620 free inodes.
| server4 | True | ['3', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105664884736 available bytes; 94.10% used; 114349570 free inodes.

server4 `/home`: 105664884736 available bytes; 94.10% used; 114349570 free inodes.

server4 `/data`: 229431050240 available bytes; 96.83% used; 224929381 free inodes.

server4 `/tmp`: 105664884736 available bytes; 94.10% used; 114349570 free inodes.

server4 `/var/tmp`: 105664884736 available bytes; 94.10% used; 114349570 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
