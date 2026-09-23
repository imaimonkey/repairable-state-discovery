# V2R cluster inventory

2026-09-23T21:08:37.753371+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['6', '7'] | ['/tmp', '/var/tmp', '/mnt/raid5'] | reference_compatible=False |

server1 `/`: 325719076864 available bytes; 81.83% used; 112501443 free inodes.

server1 `/home`: 325719076864 available bytes; 81.83% used; 112501443 free inodes.

server1 `/tmp`: 325719076864 available bytes; 81.83% used; 112501443 free inodes.

server1 `/var/tmp`: 325719076864 available bytes; 81.83% used; 112501443 free inodes.

server1 `/mnt/raid5`: 1388137672704 available bytes; 93.63% used; 337739986 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 41120591872 available bytes; 97.71% used; 110432708 free inodes.

server2 `/home`: 41120591872 available bytes; 97.71% used; 110432708 free inodes.

server2 `/tmp`: 41120591872 available bytes; 97.71% used; 110432708 free inodes.

server2 `/var/tmp`: 41120591872 available bytes; 97.71% used; 110432708 free inodes.

server2 `/mnt/raid5`: 539178225664 available bytes; 96.27% used; 445209430 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 293463400448 available bytes; 83.62% used; 114237001 free inodes.

server3 `/home`: 293463400448 available bytes; 83.62% used; 114237001 free inodes.

server3 `/data`: 52316241920 available bytes; 99.28% used; 225849573 free inodes.

server3 `/tmp`: 293463400448 available bytes; 83.62% used; 114237001 free inodes.

server3 `/var/tmp`: 293463400448 available bytes; 83.62% used; 114237001 free inodes.
| server4 | True | ['2', '3', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 106494898176 available bytes; 94.06% used; 114356047 free inodes.

server4 `/home`: 106494898176 available bytes; 94.06% used; 114356047 free inodes.

server4 `/data`: 300503228416 available bytes; 95.85% used; 225455295 free inodes.

server4 `/tmp`: 106494898176 available bytes; 94.06% used; 114356047 free inodes.

server4 `/var/tmp`: 106494898176 available bytes; 94.06% used; 114356047 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
