# V2R cluster inventory

2026-09-25T03:12:54.970166+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318940286976 available bytes; 82.21% used; 112480374 free inodes.

server1 `/home`: 318940286976 available bytes; 82.21% used; 112480374 free inodes.

server1 `/tmp`: 318940286976 available bytes; 82.21% used; 112480374 free inodes.

server1 `/var/tmp`: 318940286976 available bytes; 82.21% used; 112480374 free inodes.

server1 `/mnt/raid5`: 416120295424 available bytes; 98.09% used; 337600925 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22989914112 available bytes; 98.72% used; 110410440 free inodes.

server2 `/home`: 22989914112 available bytes; 98.72% used; 110410440 free inodes.

server2 `/tmp`: 22989914112 available bytes; 98.72% used; 110410440 free inodes.

server2 `/var/tmp`: 22989914112 available bytes; 98.72% used; 110410440 free inodes.

server2 `/mnt/raid5`: 465708343296 available bytes; 96.78% used; 445112444 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84343836672 available bytes; 95.29% used; 114156079 free inodes.

server3 `/home`: 84343836672 available bytes; 95.29% used; 114156079 free inodes.

server3 `/data`: 144815190016 available bytes; 98.00% used; 225810239 free inodes.

server3 `/tmp`: 84343836672 available bytes; 95.29% used; 114156079 free inodes.

server3 `/var/tmp`: 84343836672 available bytes; 95.29% used; 114156079 free inodes.
| server4 | True | ['6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105692839936 available bytes; 94.10% used; 114350897 free inodes.

server4 `/home`: 105692839936 available bytes; 94.10% used; 114350897 free inodes.

server4 `/data`: 48635777024 available bytes; 99.33% used; 224967232 free inodes.

server4 `/tmp`: 105692839936 available bytes; 94.10% used; 114350897 free inodes.

server4 `/var/tmp`: 105692839936 available bytes; 94.10% used; 114350897 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
