# V2R cluster inventory

2026-09-25T07:39:16.219241+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318872231936 available bytes; 82.21% used; 112480365 free inodes.

server1 `/home`: 318872231936 available bytes; 82.21% used; 112480365 free inodes.

server1 `/tmp`: 318872231936 available bytes; 82.21% used; 112480365 free inodes.

server1 `/var/tmp`: 318872231936 available bytes; 82.21% used; 112480365 free inodes.

server1 `/mnt/raid5`: 399619641344 available bytes; 98.17% used; 337558358 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22853980160 available bytes; 98.73% used; 110410512 free inodes.

server2 `/home`: 22853980160 available bytes; 98.73% used; 110410512 free inodes.

server2 `/tmp`: 22853980160 available bytes; 98.73% used; 110410512 free inodes.

server2 `/var/tmp`: 22853980160 available bytes; 98.73% used; 110410512 free inodes.

server2 `/mnt/raid5`: 334877896704 available bytes; 97.69% used; 445096493 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84437012480 available bytes; 95.29% used; 114156035 free inodes.

server3 `/home`: 84437012480 available bytes; 95.29% used; 114156035 free inodes.

server3 `/data`: 142393970688 available bytes; 98.03% used; 225812561 free inodes.

server3 `/tmp`: 84437012480 available bytes; 95.29% used; 114156035 free inodes.

server3 `/var/tmp`: 84437012480 available bytes; 95.29% used; 114156035 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105637564416 available bytes; 94.11% used; 114350349 free inodes.

server4 `/home`: 105637564416 available bytes; 94.11% used; 114350349 free inodes.

server4 `/data`: 249066582016 available bytes; 96.56% used; 225012942 free inodes.

server4 `/tmp`: 105637564416 available bytes; 94.11% used; 114350349 free inodes.

server4 `/var/tmp`: 105637564416 available bytes; 94.11% used; 114350349 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
