# V2R cluster inventory

2026-09-26T08:36:43.515511+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318745542656 available bytes; 82.22% used; 112475800 free inodes.

server1 `/home`: 318745542656 available bytes; 82.22% used; 112475800 free inodes.

server1 `/tmp`: 318745542656 available bytes; 82.22% used; 112475800 free inodes.

server1 `/var/tmp`: 318745542656 available bytes; 82.22% used; 112475800 free inodes.

server1 `/mnt/raid5`: 219086974976 available bytes; 98.99% used; 337538909 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22320852992 available bytes; 98.75% used; 110403904 free inodes.

server2 `/home`: 22320852992 available bytes; 98.75% used; 110403904 free inodes.

server2 `/tmp`: 22320852992 available bytes; 98.75% used; 110403904 free inodes.

server2 `/var/tmp`: 22320852992 available bytes; 98.75% used; 110403904 free inodes.

server2 `/mnt/raid5`: 255507251200 available bytes; 98.23% used; 445024407 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 82678235136 available bytes; 95.39% used; 114110820 free inodes.

server3 `/home`: 82678235136 available bytes; 95.39% used; 114110820 free inodes.

server3 `/data`: 123901571072 available bytes; 98.29% used; 225828708 free inodes.

server3 `/tmp`: 82678235136 available bytes; 95.39% used; 114110820 free inodes.

server3 `/var/tmp`: 82678235136 available bytes; 95.39% used; 114110820 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 106063953920 available bytes; 94.08% used; 114348137 free inodes.

server4 `/home`: 106063953920 available bytes; 94.08% used; 114348137 free inodes.

server4 `/data`: 89368494080 available bytes; 98.76% used; 224883419 free inodes.

server4 `/tmp`: 106063953920 available bytes; 94.08% used; 114348137 free inodes.

server4 `/var/tmp`: 106063953920 available bytes; 94.08% used; 114348137 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
