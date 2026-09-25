# V2R cluster inventory

2026-09-25T07:28:33.675821+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318871183360 available bytes; 82.21% used; 112480374 free inodes.

server1 `/home`: 318871183360 available bytes; 82.21% used; 112480374 free inodes.

server1 `/tmp`: 318871183360 available bytes; 82.21% used; 112480374 free inodes.

server1 `/var/tmp`: 318871183360 available bytes; 82.21% used; 112480374 free inodes.

server1 `/mnt/raid5`: 385906384896 available bytes; 98.23% used; 337558437 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22861725696 available bytes; 98.72% used; 110410510 free inodes.

server2 `/home`: 22861725696 available bytes; 98.72% used; 110410510 free inodes.

server2 `/tmp`: 22861725696 available bytes; 98.72% used; 110410510 free inodes.

server2 `/var/tmp`: 22861725696 available bytes; 98.72% used; 110410510 free inodes.

server2 `/mnt/raid5`: 343283732480 available bytes; 97.63% used; 445097412 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84447518720 available bytes; 95.29% used; 114156035 free inodes.

server3 `/home`: 84447518720 available bytes; 95.29% used; 114156035 free inodes.

server3 `/data`: 142394314752 available bytes; 98.03% used; 225812733 free inodes.

server3 `/tmp`: 84447518720 available bytes; 95.29% used; 114156035 free inodes.

server3 `/var/tmp`: 84447518720 available bytes; 95.29% used; 114156035 free inodes.
| server4 | True | ['3'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105637933056 available bytes; 94.11% used; 114350360 free inodes.

server4 `/home`: 105637933056 available bytes; 94.11% used; 114350360 free inodes.

server4 `/data`: 249101271040 available bytes; 96.56% used; 225014622 free inodes.

server4 `/tmp`: 105637933056 available bytes; 94.11% used; 114350360 free inodes.

server4 `/var/tmp`: 105637933056 available bytes; 94.11% used; 114350360 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
