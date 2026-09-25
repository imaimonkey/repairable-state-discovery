# V2R cluster inventory

2026-09-25T11:08:34.954235+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318847930368 available bytes; 82.21% used; 112478861 free inodes.

server1 `/home`: 318847930368 available bytes; 82.21% used; 112478861 free inodes.

server1 `/tmp`: 318847930368 available bytes; 82.21% used; 112478861 free inodes.

server1 `/var/tmp`: 318847930368 available bytes; 82.21% used; 112478861 free inodes.

server1 `/mnt/raid5`: 364806762496 available bytes; 98.33% used; 337555116 free inodes.
| server2 | True | ['1', '2', '3', '4', '5', '6'] | [] |

server2 `/`: 22906429440 available bytes; 98.72% used; 110409994 free inodes.

server2 `/home`: 22906429440 available bytes; 98.72% used; 110409994 free inodes.

server2 `/tmp`: 22906429440 available bytes; 98.72% used; 110409994 free inodes.

server2 `/var/tmp`: 22906429440 available bytes; 98.72% used; 110409994 free inodes.

server2 `/mnt/raid5`: 328834830336 available bytes; 97.73% used; 445088591 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84139315200 available bytes; 95.30% used; 114155494 free inodes.

server3 `/home`: 84139315200 available bytes; 95.30% used; 114155494 free inodes.

server3 `/data`: 142002720768 available bytes; 98.04% used; 225815059 free inodes.

server3 `/tmp`: 84139315200 available bytes; 95.30% used; 114155494 free inodes.

server3 `/var/tmp`: 84139315200 available bytes; 95.30% used; 114155494 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105612234752 available bytes; 94.11% used; 114350251 free inodes.

server4 `/home`: 105612234752 available bytes; 94.11% used; 114350251 free inodes.

server4 `/data`: 238643183616 available bytes; 96.70% used; 224982745 free inodes.

server4 `/tmp`: 105612234752 available bytes; 94.11% used; 114350251 free inodes.

server4 `/var/tmp`: 105612234752 available bytes; 94.11% used; 114350251 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
