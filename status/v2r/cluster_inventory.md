# V2R cluster inventory

2026-09-24T19:04:43.517500+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 323994914816 available bytes; 81.93% used; 112481464 free inodes.

server1 `/home`: 323994914816 available bytes; 81.93% used; 112481464 free inodes.

server1 `/tmp`: 323994914816 available bytes; 81.93% used; 112481464 free inodes.

server1 `/var/tmp`: 323994914816 available bytes; 81.93% used; 112481464 free inodes.

server1 `/mnt/raid5`: 416246226944 available bytes; 98.09% used; 337635352 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 54470275072 available bytes; 96.96% used; 110411909 free inodes.

server2 `/home`: 54470275072 available bytes; 96.96% used; 110411909 free inodes.

server2 `/tmp`: 54470275072 available bytes; 96.96% used; 110411909 free inodes.

server2 `/var/tmp`: 54470275072 available bytes; 96.96% used; 110411909 free inodes.

server2 `/mnt/raid5`: 495639674880 available bytes; 96.58% used; 445159471 free inodes.
| server3 | True | ['1'] | [] | reference_compatible=True |

server3 `/`: 84406796288 available bytes; 95.29% used; 114156137 free inodes.

server3 `/home`: 84406796288 available bytes; 95.29% used; 114156137 free inodes.

server3 `/data`: 152500281344 available bytes; 97.89% used; 225799934 free inodes.

server3 `/tmp`: 84406796288 available bytes; 95.29% used; 114156137 free inodes.

server3 `/var/tmp`: 84406796288 available bytes; 95.29% used; 114156137 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105660850176 available bytes; 94.10% used; 114348475 free inodes.

server4 `/home`: 105660850176 available bytes; 94.10% used; 114348475 free inodes.

server4 `/data`: 89913462784 available bytes; 98.76% used; 225267261 free inodes.

server4 `/tmp`: 105660850176 available bytes; 94.10% used; 114348475 free inodes.

server4 `/var/tmp`: 105660850176 available bytes; 94.10% used; 114348475 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
