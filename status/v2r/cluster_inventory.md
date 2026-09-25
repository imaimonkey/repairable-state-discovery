# V2R cluster inventory

2026-09-25T11:25:49.929378+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 319063871488 available bytes; 82.20% used; 112478824 free inodes.

server1 `/home`: 319063871488 available bytes; 82.20% used; 112478824 free inodes.

server1 `/tmp`: 319063871488 available bytes; 82.20% used; 112478824 free inodes.

server1 `/var/tmp`: 319063871488 available bytes; 82.20% used; 112478824 free inodes.

server1 `/mnt/raid5`: 365686259712 available bytes; 98.32% used; 337550303 free inodes.
| server2 | True | ['2', '3', '4', '5', '6'] | [] | reference_compatible=False |

server2 `/`: 22911414272 available bytes; 98.72% used; 110409978 free inodes.

server2 `/home`: 22911414272 available bytes; 98.72% used; 110409978 free inodes.

server2 `/tmp`: 22911414272 available bytes; 98.72% used; 110409978 free inodes.

server2 `/var/tmp`: 22911414272 available bytes; 98.72% used; 110409978 free inodes.

server2 `/mnt/raid5`: 327707062272 available bytes; 97.74% used; 445084391 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84131479552 available bytes; 95.31% used; 114155498 free inodes.

server3 `/home`: 84131479552 available bytes; 95.31% used; 114155498 free inodes.

server3 `/data`: 142081835008 available bytes; 98.04% used; 225814248 free inodes.

server3 `/tmp`: 84131479552 available bytes; 95.31% used; 114155498 free inodes.

server3 `/var/tmp`: 84131479552 available bytes; 95.31% used; 114155498 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105611718656 available bytes; 94.11% used; 114350251 free inodes.

server4 `/home`: 105611718656 available bytes; 94.11% used; 114350251 free inodes.

server4 `/data`: 238620073984 available bytes; 96.70% used; 224980527 free inodes.

server4 `/tmp`: 105611718656 available bytes; 94.11% used; 114350251 free inodes.

server4 `/var/tmp`: 105611718656 available bytes; 94.11% used; 114350251 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
