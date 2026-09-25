# V2R cluster inventory

2026-09-25T08:11:27.826878+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318839484416 available bytes; 82.21% used; 112480355 free inodes.

server1 `/home`: 318839484416 available bytes; 82.21% used; 112480355 free inodes.

server1 `/tmp`: 318839484416 available bytes; 82.21% used; 112480355 free inodes.

server1 `/var/tmp`: 318839484416 available bytes; 82.21% used; 112480355 free inodes.

server1 `/mnt/raid5`: 379201073152 available bytes; 98.26% used; 337557618 free inodes.
| server2 | True | ['6'] | [] | reference_compatible=False |

server2 `/`: 22842335232 available bytes; 98.73% used; 110410483 free inodes.

server2 `/home`: 22842335232 available bytes; 98.73% used; 110410483 free inodes.

server2 `/tmp`: 22842335232 available bytes; 98.73% used; 110410483 free inodes.

server2 `/var/tmp`: 22842335232 available bytes; 98.73% used; 110410483 free inodes.

server2 `/mnt/raid5`: 333841027072 available bytes; 97.69% used; 445094772 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84436582400 available bytes; 95.29% used; 114156049 free inodes.

server3 `/home`: 84436582400 available bytes; 95.29% used; 114156049 free inodes.

server3 `/data`: 142387363840 available bytes; 98.03% used; 225812013 free inodes.

server3 `/tmp`: 84436582400 available bytes; 95.29% used; 114156049 free inodes.

server3 `/var/tmp`: 84436582400 available bytes; 95.29% used; 114156049 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105625202688 available bytes; 94.11% used; 114350335 free inodes.

server4 `/home`: 105625202688 available bytes; 94.11% used; 114350335 free inodes.

server4 `/data`: 249011212288 available bytes; 96.56% used; 225008163 free inodes.

server4 `/tmp`: 105625202688 available bytes; 94.11% used; 114350335 free inodes.

server4 `/var/tmp`: 105625202688 available bytes; 94.11% used; 114350335 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
