# V2R cluster inventory

2026-09-25T10:04:47.781001+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318835290112 available bytes; 82.21% used; 112480376 free inodes.

server1 `/home`: 318835290112 available bytes; 82.21% used; 112480376 free inodes.

server1 `/tmp`: 318835290112 available bytes; 82.21% used; 112480376 free inodes.

server1 `/var/tmp`: 318835290112 available bytes; 82.21% used; 112480376 free inodes.

server1 `/mnt/raid5`: 366792568832 available bytes; 98.32% used; 337557009 free inodes.
| server2 | True | ['6'] | [] | reference_compatible=False |

server2 `/`: 22826770432 available bytes; 98.73% used; 110410468 free inodes.

server2 `/home`: 22826770432 available bytes; 98.73% used; 110410468 free inodes.

server2 `/tmp`: 22826770432 available bytes; 98.73% used; 110410468 free inodes.

server2 `/var/tmp`: 22826770432 available bytes; 98.73% used; 110410468 free inodes.

server2 `/mnt/raid5`: 316903997440 available bytes; 97.81% used; 445091222 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84418625536 available bytes; 95.29% used; 114156039 free inodes.

server3 `/home`: 84418625536 available bytes; 95.29% used; 114156039 free inodes.

server3 `/data`: 141878882304 available bytes; 98.04% used; 225810014 free inodes.

server3 `/tmp`: 84418625536 available bytes; 95.29% used; 114156039 free inodes.

server3 `/var/tmp`: 84418625536 available bytes; 95.29% used; 114156039 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105614258176 available bytes; 94.11% used; 114350276 free inodes.

server4 `/home`: 105614258176 available bytes; 94.11% used; 114350276 free inodes.

server4 `/data`: 240012328960 available bytes; 96.68% used; 224991117 free inodes.

server4 `/tmp`: 105614258176 available bytes; 94.11% used; 114350276 free inodes.

server4 `/var/tmp`: 105614258176 available bytes; 94.11% used; 114350276 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
