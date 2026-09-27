# V2R cluster inventory

2026-09-27T13:59:45.321447+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 304763604992 available bytes; 83.00% used; 112401386 free inodes.

server1 `/home`: 304763604992 available bytes; 83.00% used; 112401386 free inodes.

server1 `/tmp`: 304763604992 available bytes; 83.00% used; 112401386 free inodes.

server1 `/var/tmp`: 304763604992 available bytes; 83.00% used; 112401386 free inodes.

server1 `/mnt/raid5`: 634881769472 available bytes; 97.09% used; 337424258 free inodes.
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 13409718272 available bytes; 99.25% used; 110351816 free inodes.

server2 `/home`: 13409718272 available bytes; 99.25% used; 110351816 free inodes.

server2 `/tmp`: 13409718272 available bytes; 99.25% used; 110351816 free inodes.

server2 `/var/tmp`: 13409718272 available bytes; 99.25% used; 110351816 free inodes.

server2 `/mnt/raid5`: 527844524032 available bytes; 96.35% used; 444732388 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 78558687232 available bytes; 95.62% used; 114062779 free inodes.

server3 `/home`: 78558687232 available bytes; 95.62% used; 114062779 free inodes.

server3 `/data`: 1330869166080 available bytes; 81.61% used; 225757232 free inodes.

server3 `/tmp`: 78558687232 available bytes; 95.62% used; 114062779 free inodes.

server3 `/var/tmp`: 78558687232 available bytes; 95.62% used; 114062779 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 111009759232 available bytes; 93.81% used; 114372795 free inodes.

server4 `/home`: 111009759232 available bytes; 93.81% used; 114372795 free inodes.

server4 `/data`: 350852235264 available bytes; 95.15% used; 224727462 free inodes.

server4 `/tmp`: 111009759232 available bytes; 93.81% used; 114372795 free inodes.

server4 `/var/tmp`: 111009759232 available bytes; 93.81% used; 114372795 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
