# V2R cluster inventory

2026-09-25T14:29:20.281675+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 319158857728 available bytes; 82.20% used; 112476978 free inodes.

server1 `/home`: 319158857728 available bytes; 82.20% used; 112476978 free inodes.

server1 `/tmp`: 319158857728 available bytes; 82.20% used; 112476978 free inodes.

server1 `/var/tmp`: 319158857728 available bytes; 82.20% used; 112476978 free inodes.

server1 `/mnt/raid5`: 364134547456 available bytes; 98.33% used; 337546842 free inodes.
| server2 | True | ['3', '4', '5', '6'] | [] | reference_compatible=False |

server2 `/`: 12800294912 available bytes; 99.29% used; 110407880 free inodes.

server2 `/home`: 12800294912 available bytes; 99.29% used; 110407880 free inodes.

server2 `/tmp`: 12800294912 available bytes; 99.29% used; 110407880 free inodes.

server2 `/var/tmp`: 12800294912 available bytes; 99.29% used; 110407880 free inodes.

server2 `/mnt/raid5`: 321525075968 available bytes; 97.78% used; 445075426 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84267339776 available bytes; 95.30% used; 114154470 free inodes.

server3 `/home`: 84267339776 available bytes; 95.30% used; 114154470 free inodes.

server3 `/data`: 142211465216 available bytes; 98.03% used; 225808706 free inodes.

server3 `/tmp`: 84267339776 available bytes; 95.30% used; 114154470 free inodes.

server3 `/var/tmp`: 84267339776 available bytes; 95.30% used; 114154470 free inodes.
| server4 | True | ['2', '3'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105654374400 available bytes; 94.10% used; 114349711 free inodes.

server4 `/home`: 105654374400 available bytes; 94.10% used; 114349711 free inodes.

server4 `/data`: 231441620992 available bytes; 96.80% used; 224946429 free inodes.

server4 `/tmp`: 105654374400 available bytes; 94.10% used; 114349711 free inodes.

server4 `/var/tmp`: 105654374400 available bytes; 94.10% used; 114349711 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
