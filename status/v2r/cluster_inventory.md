# V2R cluster inventory

2026-09-25T07:56:06.721488+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318861955072 available bytes; 82.21% used; 112480375 free inodes.

server1 `/home`: 318861955072 available bytes; 82.21% used; 112480375 free inodes.

server1 `/tmp`: 318861955072 available bytes; 82.21% used; 112480375 free inodes.

server1 `/var/tmp`: 318861955072 available bytes; 82.21% used; 112480375 free inodes.

server1 `/mnt/raid5`: 386635714560 available bytes; 98.23% used; 337557946 free inodes.
| server2 | True | ['0'] | [] | reference_compatible=False |

server2 `/`: 22841720832 available bytes; 98.73% used; 110410483 free inodes.

server2 `/home`: 22841720832 available bytes; 98.73% used; 110410483 free inodes.

server2 `/tmp`: 22841720832 available bytes; 98.73% used; 110410483 free inodes.

server2 `/var/tmp`: 22841720832 available bytes; 98.73% used; 110410483 free inodes.

server2 `/mnt/raid5`: 334325952512 available bytes; 97.69% used; 445095324 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84442304512 available bytes; 95.29% used; 114156049 free inodes.

server3 `/home`: 84442304512 available bytes; 95.29% used; 114156049 free inodes.

server3 `/data`: 142389129216 available bytes; 98.03% used; 225812258 free inodes.

server3 `/tmp`: 84442304512 available bytes; 95.29% used; 114156049 free inodes.

server3 `/var/tmp`: 84442304512 available bytes; 95.29% used; 114156049 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105625665536 available bytes; 94.11% used; 114350336 free inodes.

server4 `/home`: 105625665536 available bytes; 94.11% used; 114350336 free inodes.

server4 `/data`: 249040728064 available bytes; 96.56% used; 225010479 free inodes.

server4 `/tmp`: 105625665536 available bytes; 94.11% used; 114350336 free inodes.

server4 `/var/tmp`: 105625665536 available bytes; 94.11% used; 114350336 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
